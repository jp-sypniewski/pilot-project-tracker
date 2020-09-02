from rest_framework import generics

from pilot_program.models import PilotProgram, Task
from pilot_program.api.serializers import (PilotProgramSerializer,
                                           TaskSerializer)


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        pilot_pk = self.kwargs.get('pilot_pk')
        pilot_program = generics.get_object_or_404(PilotProgram, pk=pilot_pk)

        queryset = Task.objects.filter(pilot_program=pilot_program)

        return queryset

    def perform_create(self, serializer):
        pilot_pk = self.kwargs.get('pilot_pk')
        pilot_program = generics.get_object_or_404(PilotProgram, pk=pilot_pk)

        serializer.save(pilot_program=pilot_program)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PilotProgramListCreateAPIView(generics.ListCreateAPIView):
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer


class PilotProgramDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer
