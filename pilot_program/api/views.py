from rest_framework import generics

from pilot_program.models import PilotProgram, Task
from pilot_program.api.serializers import (PilotProgramSerializer,
                                           TaskSerializer)


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PilotProgramListCreateAPIView(generics.ListCreateAPIView):
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer


class PilotProgramDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer
