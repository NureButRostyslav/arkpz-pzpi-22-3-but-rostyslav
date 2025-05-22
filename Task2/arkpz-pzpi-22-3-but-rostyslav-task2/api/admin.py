from django.contrib import admin
from .models import UserProfile, Resource, Expense, Budget

# Реєстрація моделей для адмін-панелі
admin.site.register(UserProfile)
admin.site.register(Resource)
admin.site.register(Expense)
admin.site.register(Budget)