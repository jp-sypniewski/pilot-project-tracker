from rest_framework import serializers

from pilot_program.models import PilotProgram


class PilotProgramSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PilotProgram
        fields = '__all__'