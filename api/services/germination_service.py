# services/germination_service.py
# Generated code for the germination service
from ...classes.germination import *

def create_germination_objects(data):
    temperature_data = data.get('temperature', {})
    oxygen_data = data.get('oxygen', {})
    moisture_data = data.get('moisture', {})
    
    temperature = Temperature(
        min_temp=temperature_data.get('min_temp', 0),
        max_temp=temperature_data.get('max_temp', 0)
    )
    oxygen = Oxygen(oxygen_data.get('present', 0))
    moisture = Moisture(level=moisture_data.get('level', 0))
    current_temp = temperature_data.get('current_temp') 
    return temperature, oxygen, moisture, current_temp
    
#Define to dic 
def to_json_dict(temperature, oxygen, moisture, current_temp):
    return {
        "temperature": {
            "min_temp": temperature.min_temp,
            "max_temp": temperature.max_temp,
            "is_suitable": temperature.is_suitable(current_temp)
        },
        "oxygen": {
            "present": oxygen.present,
            "is_suitable": oxygen.is_suitable()
        },
        "moisture": {
            "level": moisture.level,
        },
        "current_temp": current_temp
    }