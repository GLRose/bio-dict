from flask import Flask
from ..classes.seed import *
from ..classes.germination import *
from ..classes.enums import *

app = Flask(__name__);

# TODO: Dynamically set the class properties
@app.route('/seed_comp')

def seed_atts():
    seedcoat = SeedCoat(Texture.BUMPY, Color.BROWN, Thickness.SMALL)
    embryo = Embryo(Radicle.TAPROOT, cotyledon='', plumule='')
    stored_nutrients = StoredNutrients(carbohydrates='', lipids='', proteins='')    
    seed = Seed(seedcoat, embryo, stored_nutrients)
    dormancy = Dormancy(dormant=0)
    cotyledon = Cotyledon(type=CotyledonType.MONOCOTYLEDON, number=0)
    monocotyledon = Monocotyledon(type=CotyledonType.MONOCOTYLEDON, number=1)
    dicotyledon = Dicotyledon(type=CotyledonType.DICOTYLEDON, number=2)

    return {
        "seed_coat": {
            "color": seed.seed_coat.color.value,
            "texture": seed.seed_coat.texture.value,
            "thickness": seed.seed_coat.thickness.value,
        },
        "embryo": {
            "radicle": seed.embryo.radicle.value,
            "cotyledon": seed.embryo.cotyledon,
            "plumule": seed.embryo.plumule,
        },
        "stored_nutrients": {
            "carbohydrates": seed.stored_nutrients.carbohydrates,
            "lipids": seed.stored_nutrients.lipids,
            "proteins": seed.stored_nutrients.proteins,
        },
        "dormancy": {
            "dormant": dormancy.dormant,
        },
        "cotyledon": {
            "type": CotyledonType.MONOCOTYLEDON.value,
            "number": cotyledon.number,
        },
        "monocotyledon": {
            "type": CotyledonType.MONOCOTYLEDON.value,
            "number": monocotyledon.number,
        },
        "dicotyledon": {
            "type": CotyledonType.DICOTYLEDON.value,
            "number": dicotyledon.number,
        },
    }

@app.route('/germination')
def germination_atts():
    # germination = germination(Temperature= '', Oxygen= '', Moisture= '')
    temperature = Temperature(min_temp=0, max_temp=0)
    oxygen = Oxygen(0)
    moisture = Moisture(level=0)
    return {
        "Temperature": {
            "min_temp": temperature.min_temp,
            "max_temp": temperature.max_temp,
        },
        "Oxygen": {
            "present": oxygen.present,
        },
        "Moisture": {
            "level": moisture.level,
        },
    }



