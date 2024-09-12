from operator import itemgetter
from api.data_api import get_data
from toolz import *
from models.aircraft import Aircraft
from models.location import Location
from models.mission import Mission
from models.pilot import Pilot
from models.target import Target
from models.weather import Weather
from repository.aircraft_repository import read_aircrafts_from_json
from repository.mission_repository import write_missions_to_csv
from repository.pilot_repository import read_pilots_from_json
from repository.target_repository import read_targets_from_json
from repository.weight_repository import read_weight_from_json
from utils import haversine_distance

key = "8f2fde5c2598f2233fa89f1b07eb7eaa"
base_location_api = f"https://api.openweathermap.org/geo/1.0/direct?q="
base_weather_api = f"https://api.openweathermap.org/data/2.5/forecast?q="
base_path = "C:/Users/user/PycharmProjects/air_force_strikes/"
this_day = "2024-09-13 00:00:00"
my_city = "Jerusalem"
all_targets = read_targets_from_json(f"{base_path}/jsons/targets.json")
all_pilots = read_pilots_from_json(f"{base_path}jsons/pilots.json")
all_aircrafts = read_aircrafts_from_json(f"{base_path}jsons/aircrafts.json")
weighets = read_weight_from_json(f"{base_path}jsons/weights.json")

def convert_data_to_weather_model(city: str, data) -> Weather:
    return Weather(
        city=city,
        weather_main=get_in(['weather',0, 'main'], data),
        clouds_all=get_in(['clouds', 'all'], data),
        wind_speed=get_in(['wind', 'speed'], data)
    )

def convert_data_to_location_model(data: tuple[2]) -> Location:
    return Location(
        lat = data[0],
        lon = data[1]
    )
def weather_score(weather: str) -> float:
    if weather== 'Clear':
        return 1
    elif weather == 'Windy':
        return 0.5
    else:
        return 0.2

def get_mission_score(priority, distance: float, speed: int, fuel_capacity: int, pilot_skill: int, weather: str) -> float:
    return ((distance/100 * weighets.distance +
            (speed * 0.5 + fuel_capacity * 0.5)/10000 * weighets.aircraft_type +
            pilot_skill / 10 * weighets.pilot_skill +
            weather_score(weather) * weighets.weather_conditions +
            (distance * 100 * weighets.execution_time) / speed)/100 + priority/10)

def convert_to_mission(target: Target, pilot: Pilot, distance: float, aircraft :Aircraft, weather: Weather) -> Mission:
    return Mission(
        target_city=target.target_city,
        priority=target.priority,
        assigned_pilot=pilot.name,
        assigned_aircraft=aircraft.type,
        distance=distance,
        weather_conditions=weather.weather_main,
        pilot_skill=pilot.skill,
        aircraft_speed=aircraft.speed,
        fuel_capacity=aircraft.fuel_capacity,
        mission_fit_score=get_mission_score
        (target.priority,distance, aircraft.speed, aircraft.fuel_capacity, pilot.skill, weather.weather_main)
    )


get_location = compose(
    first,
    partial(map, lambda l: (l['lat'], l['lon'])),
    get_data,
    lambda city: f'{base_location_api}{city}&appid={key}'
)

get_weather = compose(
    first,
    partial(filter, lambda w: w["dt_txt"] == this_day),
    itemgetter("list"),
    get_data,
    lambda city: f'{base_weather_api}{city}&appid={key}'
)

my_location = convert_data_to_location_model(get_location(my_city))

def create_all_missions():
    all_missions = []
    for t in all_targets:
        location = convert_data_to_location_model(get_location(t.target_city))
        distance = haversine_distance(location.lat, location.lon, my_location.lat, my_location.lon)
        weather = convert_data_to_weather_model(t.target_city, get_weather(t.target_city))
        for p in all_pilots:
            for a in all_aircrafts:
                all_missions += [convert_to_mission(t, p, distance, a, weather)]
    return all_missions


