import json
from models.weight import Weight

class WeightEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Weight):
            return obj.__dict__
        return super().default(obj)

def write_weight_to_json(weight: Weight, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(weight.__dict__, jsonfile, indent=4)

def read_weight_from_json(filename: str) -> Weight:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Weight(data['distance'],
                  data['aircraft_type'],
                  data['pilot_skill'],
                  data['weather_conditions'],
                  data["execution_time"]
                  )