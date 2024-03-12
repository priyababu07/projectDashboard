from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# views.py

from rest_framework import generics
from .models import Machine, MachinePowerHistory
from .serializers import MachineSerializer, MachinePowerHistorySerializer

class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachinePowerHistoryListCreateView(generics.ListCreateAPIView):
    queryset = MachinePowerHistory.objects.all()
    serializer_class = MachinePowerHistorySerializer

class MachinePowerHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MachinePowerHistory.objects.all()
    serializer_class = MachinePowerHistorySerializer

csrf_exempt
def store_machine_data_view(request):
    if request.method == 'POST':
        # Handle the incoming data and store it in your database
        # You can access the data using request.POST or request.body

        # Example response
        return JsonResponse({'status': 'Data stored successfully'})
    else:
        return JsonResponse({'status': 'Invalid request method'}, status=405)