# backapp/machinedata.py
import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django
django.setup()






import time
import serial
from backapp.models import Machine

arduino_data = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1)

while True:
    while arduino_data.inWaiting() == 0:
        pass

    data_packet = arduino_data.readline().decode('utf-8').strip().split(',')

    # Assuming the order of data_packet is machine_name, base_power_consumption, production_rate
    machine_name, base_power_consumption, production_rate = data_packet

    # Save data to the database using the Django model
    machine_data = Machine.objects.create(
        name=machine_name,
        base_power_consumption=int(base_power_consumption),
        production_rate=int(production_rate),
    )

    # You can perform additional operations if needed

    time.sleep(1)

