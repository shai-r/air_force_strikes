import json
from models.aircraft import Aircraft
from typing import List

class AircraftEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Aircraft):
            return obj.__dict__
        return super().default(obj)

def write_aircrafts_to_json(aircrafts: List[Aircraft], filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(aircrafts, jsonfile, cls=AircraftEncoder, indent=4)

def read_aircrafts_from_json(filename: str) -> List[Aircraft]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Aircraft(aircraft['type'], aircraft['speed'], aircraft['fuel_capacity'])
            for aircraft in data]

def write_aircraft_to_json(aircraft: Aircraft, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(aircraft.__dict__, jsonfile, indent=4)

def read_aircraft_from_json(filename: str) -> Aircraft:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Aircraft(data['type'], data['speed'], data['fuel_capacity'])

# target_city,
#                  priority,
#                  assigned_pilot,
#                  assigned_aircraft,
#                  distance,
#                  weather_conditions,
#                  pilot_skill,
#                  aircraft_speed,
#                  fuel_capacity,
#                  mission_fit_score