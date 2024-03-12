# urls.py

from django.urls import path
from .views import MachineListCreateView, MachineDetailView, MachinePowerHistoryListCreateView, MachinePowerHistoryDetailView,store_machine_data_view

urlpatterns = [
    path('machines/', MachineListCreateView.as_view(), name='machine-list-create'),
    path('machines/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),

    path('machine-power-history/', MachinePowerHistoryListCreateView.as_view(), name='machine-power-history-list-create'),
    path('machine-power-history/<int:pk>/', MachinePowerHistoryDetailView.as_view(), name='machine-power-history-detail'),
    path('store_machine_data/', store_machine_data_view, name='store_machine_data'),
]
