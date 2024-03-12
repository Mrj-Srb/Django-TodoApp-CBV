from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = 'user'

    def __str__(self):
        return f"{self.id} - {self.user}"
