# models.py

from django.db import models




class Machine(models.Model):
    name = models.CharField(max_length=255)
    base_power_consumption = models.FloatField()
    historical_peak_usage = models.CharField(max_length=10)  # Change to CharField for more detailed information
    production_rate = models.FloatField()

class MachinePowerHistory(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    power_consumption = models.FloatField()
    is_peak = models.BooleanField()

    def save(self, *args, **kwargs):
        # Ensure is_peak is equal to historical_peak_usage of the associated machine
        self.is_peak = self.machine.historical_peak_usage
        super().save(*args, **kwargs)

class MachineData(models.Model):
    machine_name = models.CharField(max_length=50)
    base_power_consumption = models.IntegerField()
    production_rate = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)




