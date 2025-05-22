from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, ResourceViewSet, ExpenseViewSet, BudgetViewSet, login_view, analytics_view

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'budgets', BudgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('analytics/', analytics_view, name='analytics'),
]