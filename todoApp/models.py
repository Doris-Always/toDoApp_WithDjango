from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Todo(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=40)
    completed_task = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.datetime}  {self.body} {self.completed_task}'


#
# class MyUser(models.Model):
#     username = models.CharField(max_length=50)
#     todo = models.ForeignKey(Todo,on_delete=models.CASCADE)


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email Address")
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
