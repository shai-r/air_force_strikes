import csv
from typing import List
from models.mission import Mission
from toolz import  pipe, partial

def read_missions_from_csv(filepath: str) -> List[Mission]:
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            return pipe(
                [row for row in reader],
                partial(map, lambda m: Mission(
                    m['target_city'],
                    m['priority'],
                    m['assigned_pilot'],
                    m['assigned_aircraft'],
                    m['distance'],
                    m['weather_conditions'],
                    m['pilot_skill'],
                    m['aircraft_speed'],
                    m['fuel_capacity'],
                    m['mission_fit_score'],
                )),
                list
            )
    except Exception as e:
        print(e)
        return []



def write_mission_to_csv(mission: Mission, filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['target_city',
                                                             'priority',
                                                             'assigned_pilot',
                                                             'assigned_aircraft',
                                                             'distance',
                                                             'weather_conditions',
                                                             'pilot_skill',
                                                             'aircraft_speed',
                                                             'fuel_capacity',
                                                             'mission_fit_score'
                                                             ]
                                        )
            csv_writer.writeheader()

            csv_writer.writerow({
                'target_city': mission.target_city,
                'priority': mission.priority,
                'assigned_pilot': mission.assigned_pilot,
                'assigned_aircraft': mission.assigned_aircraft,
                'distance': mission.distance,
                'weather_conditions': mission.weather_conditions,
                'pilot_skill': mission.pilot_skill,
                'aircraft_speed': mission.aircraft_speed,
                'fuel_capacity': mission.fuel_capacity,
                'mission_fit_score': mission.mission_fit_score
            })
    except Exception as e:
        print(e)

def write_missions_to_csv(missions: List[Mission], filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['target_city',
                                                             'priority',
                                                             'assigned_pilot',
                                                             'assigned_aircraft',
                                                             'distance',
                                                             'weather_conditions',
                                                             'pilot_skill',
                                                             'aircraft_speed',
                                                             'fuel_capacity',
                                                             'mission_fit_score'
                                                             ])
            csv_writer.writeheader()

            for mission in missions:
                csv_writer.writerow({
                    'target_city': mission.target_city,
                    'priority': mission.priority,
                    'assigned_pilot': mission.assigned_pilot,
                    'assigned_aircraft': mission.assigned_aircraft,
                    'distance': mission.distance,
                    'weather_conditions': mission.weather_conditions,
                    'pilot_skill': mission.pilot_skill,
                    'aircraft_speed': mission.aircraft_speed,
                    'fuel_capacity': mission.fuel_capacity,
                    'mission_fit_score': mission.mission_fit_score
                })
    except Exception as e:
        print(e)
