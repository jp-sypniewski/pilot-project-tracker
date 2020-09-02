from rest_framework import generics

from pilot_program.models import PilotProgram
from pilot_program.api.serializers import PilotProgramSerializer


class PilotProgramListCreateAPIView(generics.ListCreateAPIView):
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer


class PilotProgramDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer