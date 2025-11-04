from flask import Flask
from .seed import *

app = Flask(__name__);

@app.route('/seedcoat')
def seed_coat_atts(): 
    seed_coat = SeedCoat(Texture.BUMPY, Color.BROWN, Thickness.SMALL)
    return {
        "color": seed_coat.color.value,
        "texture": seed_coat.texture.value,
        "thickness": seed_coat.thickness.value,
    }

# TODO: Dynamically set the class properties
@app.route('/embryo')
def embryo_atts():
    embryo = Embryo(Radicle.TAPROOT, cotyledon='', plumule='') 
    return {
       "radicle": embryo.radicle.value, 
       "cotyledon": embryo.cotyledon,
       "plumule": embryo.plumule,
    } 

# @app.route('/storedNutrients')
# def stored_nutrient_atts():
#     stored_nutrients = StoredNutrients(StoredNutrients.car) 
#     return {
#     } 



