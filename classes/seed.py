from .enums import *
# A seed consists of a seed coat, an embryo, and stored nutrients

class Seed: 
  def __init__(self, seed_coat, embryo, stored_nutrients):
    self.seed_coat = seed_coat
    self.embryo = embryo
    self.stored_nutrients =  stored_nutrients

# The conventional understanding of the role of the seed coat is that it provides a protective layer for the developing zygote
class SeedCoat: 
  def __init__(self, texture, color, thickness): 
    self.texture = texture
    self.color = color
    self.thickness = thickness
    
# A seed embryo consists of the radicle(embryonic root), plumule(shoot), and cotyledon(s)
class Embryo:
  def __init__(self, radicle, plumule, cotyledon):
    self.radicle = radicle
    self.plumule = plumule
    self.cotyledon = cotyledon

# Stored nutrients in a seed consist of carbohydrates, lipids(oils), and proteins
class StoredNutrients:
  def __init__(self, carbohydrates, lipids, proteins):
    self.carbohydrates = carbohydrates 
    self.lipids = lipids
    self.proteins = proteins

class Dormancy: 
  def __init__(self, dormant):
    self.dormant = dormant

  def __bool__(self):
    return self.dormant != 0
  
class Cotyledon: 
  def __init__(self, type, number):
    self.type = type
    self.number = number

class Monocotyledon(Cotyledon):
  def __init__(self, type = CotyledonType.MONOCOTYLEDON, number = 1):
    super().__init__(type, number)

class Dicotyledon(Cotyledon):
  def __init__(self, type = CotyledonType.DICOTYLEDON, number = 2):
    super().__init__(type, number)


