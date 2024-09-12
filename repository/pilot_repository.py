import json
from models.pilot import Pilot
from typing import List

class PilotEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pilot):
            return obj.__dict__
        return super().default(obj)

def write_pilots_to_json(pilots: List[Pilot], filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(pilots, jsonfile, cls=PilotEncoder, indent=4)

def read_pilots_from_json(filename: str) -> List[Pilot]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Pilot(pilot['name'], pilot['skill']) for pilot in data]

def write_pilot_to_json(pilot: Pilot, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(pilot.__dict__, jsonfile, indent=4)

def read_pilot_from_json(filename: str) -> Pilot:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Pilot(data['name'], data['skill'])
