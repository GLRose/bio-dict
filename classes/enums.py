from enum import Enum

# SEED ENUMS
class Texture(Enum):
    BUMPY = "bumpy"
    SMOOTH = "smooth"
    ROUGH = "rough"

class Color(Enum):
    YELLOW = "yellow"
    DARK_YELLOW = "dark yellow"
    BROWN_YELLOW = "brown yellow"
    LIGHT_BROWN = "light brown"
    BROWN = "brown"
    BLACK = "black"

# Ultimately include actual size in mm
class Thickness(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class Radicle(Enum):
    TAPROOT = "taproot"
    FOOD_STORAGE = "food storage"

class StoredNutriends(Enum):
    CARBOHYDRATES = "carbohydrates"
    LIPIDS = "lipids"
    PROTEINS = "proteins"

#GERMINATION ENUMS

class Gibberellin(Enum):
    ACID19 = "acid19"
    ACID20 = "acid20"