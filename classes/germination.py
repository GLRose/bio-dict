# Conditions to germinate seeds

# Temperature
class Temperature:
    def __init__(self, min_temp: float, max_temp: float):
        self._min_temp = min_temp
        self._max_temp = max_temp
    
    @property
    def min_temp(self):
        return self._min_temp
    
    @property 
    def max_temp(self):
        return self._max_temp

    def is_suitable(self, current_temp: float) -> bool:
        return self.min_temp <= current_temp <= self.max_temp
# Oxygen
class Oxygen: 
    def __init__(self, present: bool):
        self.present = present

    def is_suitable(self) -> bool:
        return self.present != 0

# Moisture
# I need to decide what the best metric for determining moisture level is or how important the variance is for a seed
class Moisture:
    def __init__(self, level: float):
        self.level = level

    def is_suitable(self, current_moisture: float) -> bool:
        return self.level == current_moisture



