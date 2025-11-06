from flask import Flask
from ..classes.seed import *

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

@app.route('/nutrients')
def stored_nutrient_atts():
    stored_nutrients = StoredNutrients(carbohydrates='', lipids='', proteins='') 
    return {
        "carbs": stored_nutrients.carbohydrates,
        "lipids": stored_nutrients.lipids,
        "proteins": stored_nutrients.proteins,
    }



