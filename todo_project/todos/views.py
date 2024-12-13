from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['completed', 'tags']
    ordering_fields = ['due_date', 'created_at', 'title']
    ordering = ['-created_at']

    @action(detail=True, methods=['patch'], url_path='mark_complete')
    def mark_complete(self, request, pk=None):
        """
        Перевод задачи в выполненные.
        """
        try:
            task = self.get_object()
            task.completed = True
            task.save()
            return Response({'detail': 'Задача успешно выполнена.'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'detail': 'Задача не найдена.'}, status=status.HTTP_404_NOT_FOUND)


