# Conditions to germinate seeds

# Temperature
class Temperature:
    def __init__(self, min_temp: float, max_temp: float):
        self.min_temp = min_temp
        self.max_temp = max_temp
# Oxygen
class Oxygen: 
    def __init__(self, present):
        self.present = present
    
    def __bool__(self):
        return self.present != 0
# Moisture
class Moisture:
    def __init__(self, level: float):
        self.level = level

    def __bool__(self):
        return self.level > 0