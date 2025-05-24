from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    login_view,
    UserProfileViewSet,
    ResourceViewSet,
    ExpenseViewSet,
    BudgetViewSet,
    ActionLogViewSet,
    analytics_view,
    create_user,
    delete_user,
)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='userprofile')
router.register(r'resources', ResourceViewSet)
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'budgets', BudgetViewSet)
router.register(r'action-logs', ActionLogViewSet, basename='actionlog')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('analytics/', analytics_view, name='analytics'),
    path('admin/users/create/', create_user, name='create_user'),
    path('admin/users/delete/<int:user_id>/', delete_user, name='delete_user'),
]
