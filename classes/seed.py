from enums import Texture, Color, Thickness
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
# TODO: Always refer to variations to find the components of said component
seed_coat = SeedCoat(Texture.BUMPY, Color.BROWN, Thickness.SMALL)

print(seed_coat.texture.value, seed_coat.color.value, seed_coat.thickness.value)

# A seed embryo consists of the radicle(embryonic root), plumule(shoot), and cotyledon(s)
class Embryo:
  def __init__(self, radicle, plumule, cotyledon)
    self.radicle = radicle
    self.plumule = plumule
    self.cotyledon = cotyledon

# Stored nutrients in a seed consist of carbohydrates, lipids(oils), and proteins
class StoredNutrients:
  def __init__(self, carbohydrates, lipids, proteins)
    self.carohydrates = carbohydrates 
    self.lipids = lipids
    self.proteins = proteins
# I need to handle monocotyledons and dicotyledons potentially with inheritance or extensiton

# This is how we set multipart parameters to a single param 
seed_coat = SeedCoat(Texture.BUMPY, Color.BROWN, Thickness.SMALL)
seed = Seed(seed_coat, 'hi', 'bye')
print(seed.seed_coat.color)