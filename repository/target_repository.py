import json
from models.target import Target
from typing import List

class TargetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Target):
            return obj.__dict__
        return super().default(obj)

def write_targets_to_json(targets: List[Target], filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(targets, jsonfile, cls=TargetEncoder, indent=4)

def read_targets_from_json(filename: str) -> List[Target]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Target(target['target_city'], target['priority']) for target in data]

def write_target_to_json(target: Target, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(target.__dict__, jsonfile, indent=4)

def read_target_from_json(filename: str) -> Target:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Target(data['target_city'], data['priority'])
