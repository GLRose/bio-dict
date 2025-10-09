from enum import Enum
from classes.seed import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Dormancy
from classes.seed import *
def test_not_dormant():
  x = Dormancy(0)
  assert not x

def test_dormant():
  x = Dormancy(1)
  assert x

#Moncotyledon and Dicotyledon
def test_cotyledon():
  x = Monocotyledon("fleshy")
  assert x.type == "fleshy"
  assert x.number == 1


#TODO break class testing out into separate tests
# This is how we set multipart parameters to a single param 
seed_coat = SeedCoat(Texture.BUMPY, Color.BROWN, Thickness.SMALL)
seed = Seed(seed_coat, 'hi', 'bye')
print(seed.seed_coat.color)
logger.info(seed.seed_coat.color)

