from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import UserProfile, Resource, Expense, Budget
from .serializers import (
    UserProfileSerializer,
    ResourceSerializer,
    ExpenseSerializer,
    BudgetSerializer,
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
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]


# --- Analytics View ---
@swagger_auto_schema(
    method='get',
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
    expenses = Expense.objects.all()
    total_cost = sum(expense.total_cost for expense in expenses)
    return Response({'total_cost': total_cost}, status=status.HTTP_200_OK)
