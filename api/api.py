from flask import Flask, request, jsonify
from ..classes.seed import *
from ..classes.germination import *
from ..classes.enums import *

app = Flask(__name__)

# TODO: Dynamically set the class properties
@app.route('/seed_comp', methods=['GET'])

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

@app.route('/germination_data', methods=['GET'])
def germination_atts():
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

@app.route('/germination', methods=['POST'])
def germination_test():
    data = request.get_json() or {}
    
    temp_data = data.get('temperature', {})
    oxygen_data = data.get('oxygen', {})
    moisture_data = data.get('moisture', {})
    
    # Create objects with dynamic values from payload
    temperature = Temperature(
        min_temp=temp_data.get('min_temp', 0),
        max_temp=temp_data.get('max_temp', 0)
    )
    oxygen = Oxygen(oxygen_data.get('present', 0))
    moisture = Moisture(level=moisture_data.get('level', 0))
    
    return jsonify({
        "temperature": {
            "min_temp": temperature.min_temp,
            "max_temp": temperature.max_temp,
            "is_suitable": temperature.is_suitable(temp_data['current_temp'])
        },
        "oxygen": {
            "present": oxygen.present,
            "is_suitable": oxygen.is_suitable()
        },
        "moisture": {
            "level": moisture.level,
        },
        "received_data": data
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


