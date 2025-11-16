# services/seed_service.py
from ...classes.seed import *
from ...classes.enums import *

def create_seed_objects(data):
    seedcoat_data = data.get('seed_coat', {})
    seed_coat = SeedCoat(
        texture=Texture[seedcoat_data.get('texture', 'BUMPY')],
        color=Color[seedcoat_data.get('color', 'BROWN')],
        thickness=Thickness[seedcoat_data.get('thickness', 'SMALL')]
    )
    
    embryo_data = data.get('embryo', {})
    embryo = Embryo(
        radicle=Radicle[embryo_data.get('radicle', 'TAPROOT')],
        cotyledon=embryo_data.get('cotyledon', ''),
        plumule=embryo_data.get('plumule', '')
    )
    
    nutrients_data = data.get('stored_nutrients', {})
    stored_nutrients = StoredNutrients(
        carbohydrates=nutrients_data.get('carbohydrates', ''),
        lipids=nutrients_data.get('lipids', ''),
        proteins=nutrients_data.get('proteins', '')
    )
    
    seed = Seed(seed_coat, embryo, stored_nutrients)
    
    dormancy_data = data.get('dormancy', {})
    dormancy = Dormancy(dormant=dormancy_data.get('dormant', 0))

    # This is hardcoded for now, but will be dynamic in the future. Pls fix 
    cotyledon = Cotyledon(type=CotyledonType.MONOCOTYLEDON, number=data['cotyledon']['number'])
    monocotyledon = Monocotyledon(type=CotyledonType.MONOCOTYLEDON, number=data['monocotyledon']['number'])
    dicotyledon = Dicotyledon(type=CotyledonType.DICOTYLEDON, number=data['dicotyledon']['number'])
    
    return seed, dormancy, cotyledon, monocotyledon, dicotyledon

def to_json_dict(seed, dormancy, cotyledon, monocotyledon, dicotyledon):
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
