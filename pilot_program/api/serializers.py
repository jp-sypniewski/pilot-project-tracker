from rest_framework import serializers

from pilot_program.models import PilotProgram, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class PilotProgramSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PilotProgram
        fields = '__all__'
