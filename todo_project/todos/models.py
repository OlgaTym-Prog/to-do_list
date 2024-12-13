from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='todos')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name