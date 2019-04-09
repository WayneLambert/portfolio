from django.conf import settings
from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    open_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now=True, auto_now_add=False)
    due_date = models.DateField(auto_now=False)
    completed_date = models.DateField()
    draft = models.BooleanField(default=False)
    PRIORITIES = (
        ('HIGH', '(1) High'),
        ('MEDIUM', '(2) Medium'),
        ('LOW', '(3) Low'),
        )
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='MEDIUM')
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey('Owner', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-due_date", "priority"]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField

    def __str__(self):
        return self.title


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
