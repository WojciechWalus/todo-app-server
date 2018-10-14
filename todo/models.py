from django.db import models

# Create your models here.


class TodoNote(models.Model):
    user = models.CharField(max_length=300)
    importance = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.user, self.title)


class TodoUser(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=300)
    user_token = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class TodoApps(models.Model):
    name = models.CharField(max_length=50)
    appkey = models.CharField(max_length=30)
    canMakeUsers = models.BooleanField(default=False)
    canDeleteUsers = models.BooleanField(default=False)
    canMakeNotes = models.BooleanField(default=False)
    canDeleteNotes = models.BooleanField(default=False)
    canEditNotes = models.BooleanField(default=False)

    def __str__(self):
        return self.name
