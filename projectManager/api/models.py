from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):
    created_at = models.DateField('creation date', default = date.today)

    def __str__(self):
        return f'{self.username} - {self.email} - {self.created_at}'

class Project(models.Model):
    title = models.CharField('project title', max_length = 100)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'project')
    created_at = models.DateField('creation date', default = date.today)

    def __str__(self):
        return f'{self.title} - {self.created_at}'

class Task(models.Model):
    project = models.ForeignKey(Project, verbose_name = 'project task')
    title = models.CharField('task title', max_length = 100)
    content = models.CharField('task content', max_length = 500)

    def __str__(self):
        return f'{self.title} - {self.project}'

