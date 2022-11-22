import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class UserProfile(AbstractUser):
    pass
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.username

class Fibonacci(models.Model):
    input_value = models.IntegerField()
    fibonacci_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=(255),default="pending")
    user_id = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return str(self.input_value) + ' -> ' + str(self.fibonacci_value) + ', Inputted by: ' + str(self.user_id)
