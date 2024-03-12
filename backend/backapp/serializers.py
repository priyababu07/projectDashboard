# serializers.py

from rest_framework import serializers
from .models import Machine, MachinePowerHistory,MachineData

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class MachinePowerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MachinePowerHistory
        fields = '__all__'

class MachineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineData
        fields = '__all__'