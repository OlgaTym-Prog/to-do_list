from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['completed', 'tags']
    ordering_fields = ['due_date', 'created_at', 'title']
    ordering = ['-created_at']
