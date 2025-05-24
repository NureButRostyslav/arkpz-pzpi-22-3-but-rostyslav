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

    def check_availability(self):
        # Перевірка, чи ресурс вільний у вказаний час (MF2)
        conflicts = Expense.objects.filter(
            resource=self.resource,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)
        return not conflicts.exists()

    def check_budget(self):
        # Перевірка, чи витрата не перевищує бюджет (MF7)
        profile = UserProfile.objects.get(user=self.user)
        budget = Budget.objects.filter(corporate_account_id=profile.corporate_account_id).first()
        if not budget:
            return True  # Немає бюджету — дозволяємо
        total_expenses = Expense.objects.filter(
            user__userprofile__corporate_account_id=profile.corporate_account_id
        ).exclude(id=self.id).aggregate(models.Sum('total_cost'))['total_cost__sum'] or 0
        return total_expenses + self.total_cost <= budget.limit_amount

    def save(self, *args, **kwargs):
        # Перевірки перед збереженням
        if not self.check_availability():
            raise ValueError("Resource is not available at this time")
        if not self.check_budget():
            raise ValueError("Expense exceeds budget limit")
        # Розрахунок витрат
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

class ActionLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin.username} - {self.action} at {self.timestamp}"
