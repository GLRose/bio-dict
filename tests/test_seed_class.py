import sys
import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Get the parent directory (the folder containing "classes")
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes')))
from seed import *

def test_not_dormant():
  x = Dormancy(0)
  assert not x

def test_dormant():
  x = Dormancy(1)
  assert x

#TODO break class testing out into separate tests
# This is how we set multipart parameters to a single param 
seed_coat = SeedCoat(Texture.BUMPY, Color.BROWN, Thickness.SMALL)
seed = Seed(seed_coat, 'hi', 'bye')
print(seed.seed_coat.color)
logger.info(seed.seed_coat.color)

