from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    corporate_account_id = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.user.username} (Account {self.corporate_account_id})"

class Resource(models.Model):
    name = models.CharField(max_length=100)
    cost_per_hour = models.FloatField()

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.FloatField()

    def save(self, *args, **kwargs):
        # Автоматичний розрахунок витрат (MF2)
        if self.start_time and self.end_time:
            time_diff = (self.end_time - self.start_time).total_seconds() / 3600
            self.total_cost = time_diff * self.resource.cost_per_hour
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.resource.name}"

class Budget(models.Model):
    corporate_account_id = models.IntegerField()
    limit_amount = models.FloatField()

    def __str__(self):
        return f"Budget {self.id} for account {self.corporate_account_id}"