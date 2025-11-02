# Simulate germination conditions: Temperature, Oxygen, Moisture 

from enum import Enum
from classes.germination import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Temperature
min_temp = 10
max_temp = 30
def test_sutable_temperature():
  wheat_seed = Temperature(min_temp=min_temp, max_temp=max_temp)
  assert wheat_seed.is_suitable(10)
  
def test_unsuitable_temperature():
  wheat_seed = Temperature(min_temp=min_temp, max_temp=max_temp)
  assert not wheat_seed.is_suitable(1)

#Oxygen
def test_oxygen_presence():
  x = Oxygen(1)
  assert x.present

def test_oxygen_absense():
  x = Oxygen(0)
  assert not x.present

#Moisture
def test_suitable_moisture_level():
  capsicum_seed = Moisture(100)
  assert capsicum_seed.is_suitable(100)

def test_unsuitable_moisture_level():
  capsicum_seed = Moisture(90)
  assert not capsicum_seed.is_suitable(30)


