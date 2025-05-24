from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Sum, Q

from .models import UserProfile, Resource, Expense, Budget, ActionLog
from .serializers import (
    UserProfileSerializer,
    ResourceSerializer,
    ExpenseSerializer,
    BudgetSerializer,
    ActionLogSerializer,
)

# --- Login View ---
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Ім’я користувача'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль'),
        },
    ),
    responses={
        200: openapi.Response(
            description='Успішний вхід',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'message': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        ),
        401: openapi.Response(description='Невірні облікові дані'),
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# --- ViewSets for Models ---
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Забороняємо створення профілів через цей ендпоінт
        return Response(
            {'error': 'User creation is only allowed via /api/admin/users/create/'},
            status=status.HTTP_403_FORBIDDEN
        )

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Expense.objects.all()
        return Expense.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        resource = serializer.validated_data['resource']
        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']

        # Перевірка доступності ресурсу
        overlapping_expenses = Expense.objects.filter(
            resource=resource,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping_expenses.exists():
            return Response(
                {"error": "Resource is not available at this time"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Перевірка бюджету
        try:
            profile = UserProfile.objects.get(user=user)
            budget = Budget.objects.filter(corporate_account_id=profile.corporate_account_id).first()
            if budget:
                total_cost = resource.cost_per_hour * (
                    (end_time - start_time).total_seconds() / 3600
                )
                current_expenses = Expense.objects.filter(
                    user__userprofile__corporate_account_id=profile.corporate_account_id
                ).aggregate(total=Sum('total_cost'))['total'] or 0
                if current_expenses + total_cost > budget.limit_amount:
                    return Response(
                        {"error": "Budget limit exceeded"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "User profile not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

class ActionLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActionLog.objects.all()
    serializer_class = ActionLogSerializer
    permission_classes = [IsAdminUser]

# --- Analytics View ---
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('user_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='User ID'),
        openapi.Parameter('start_date', openapi.IN_QUERY, type=openapi.TYPE_STRING, format='date', description='Start date (YYYY-MM-DD)'),
        openapi.Parameter('end_date', openapi.IN_QUERY, type=openapi.TYPE_STRING, format='date', description='End date (YYYY-MM-DD)'),
    ],
    responses={
        200: openapi.Response(
            description='Сума витрат',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'total_cost': openapi.Schema(type=openapi.TYPE_NUMBER)}
            )
        )
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def analytics_view(request):
    expenses = Expense.objects.all() if request.user.is_staff else Expense.objects.filter(user=request.user)
    user_id = request.query_params.get('user_id')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    if user_id and request.user.is_staff:
        expenses = expenses.filter(user_id=user_id)
    if start_date:
        expenses = expenses.filter(start_time__gte=start_date)
    if end_date:
        expenses = expenses.filter(end_time__lte=end_date)

    total_cost = expenses.aggregate(total=Sum('total_cost'))['total'] or 0
    return Response({'total_cost': total_cost}, status=status.HTTP_200_OK)

# --- Admin Functions ---
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password', 'email', 'corporate_account_id'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'corporate_account_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        }
    ),
    responses={201: 'User created', 400: 'Invalid data'}
)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    corporate_account_id = request.data.get('corporate_account_id')

    if not all([username, password, email, corporate_account_id]):
        return Response(
            {'error': 'Missing required fields'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Перевірка унікальності corporate_account_id
        if UserProfile.objects.filter(corporate_account_id=corporate_account_id).exists():
            return Response(
                {'error': 'Corporate account ID already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, password=password, email=email)
        # Перевірка, чи профіль уже створено сигналом
        if not hasattr(user, 'userprofile'):
            UserProfile.objects.create(user=user, corporate_account_id=corporate_account_id)
        else:
            # Оновлюємо corporate_account_id, якщо профіль існує
            user.userprofile.corporate_account_id = corporate_account_id
            user.userprofile.save()

        ActionLog.objects.create(
            admin=request.user,
            action=f'Created user {username} at {timezone.now()}'
        )
        print(f"Creating ActionLog for admin {request.user.username}, action: Created user {username}")
        return Response(
            {'message': 'User created'},
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

@swagger_auto_schema(
    method='delete',
    manual_parameters=[openapi.Parameter('user_id', openapi.IN_PATH, type=openapi.TYPE_INTEGER, description='User ID')],
    responses={204: 'User deleted', 404: 'User not found'}
)
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        username = user.username
        UserProfile.objects.filter(user=user).delete()
        user.delete()
        ActionLog.objects.create(
            admin=request.user,
            action=f'Deleted user {username} at {timezone.now()}'
        )
        print(f"Creating ActionLog for admin {request.user.username}, action: Deleted user {username}")
        return Response(
            {'message': 'User deleted'},
            status=status.HTTP_204_NO_CONTENT
        )
    except User.DoesNotExist:
        return Response(
            {'error': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )
