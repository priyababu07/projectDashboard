from django.contrib import admin
from .models import Machine, MachinePowerHistory

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_power_consumption', 'historical_peak_usage', 'production_rate')
    list_filter = ('historical_peak_usage',)  # Adds a filter for historical_peak_usage
    search_fields = ('name',)  # Adds a search bar for the 'name' field

@admin.register(MachinePowerHistory)
class MachinePowerHistoryAdmin(admin.ModelAdmin):
    list_display = ('machine', 'timestamp', 'power_consumption', 'is_peak')
    list_filter = ('is_peak',)  # Adds a filter for is_peak
    search_fields = ('machine__name',)  # Adds a search bar for the 'machine__name' field

