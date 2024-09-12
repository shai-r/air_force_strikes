class Weight:

    def __init__(self,
                 distance,
                 aircraft_type,
                 pilot_skill,
                 weather_conditions,
                 execution_time):
        self.distance = distance
        self.aircraft_type = aircraft_type
        self.pilot_skill = pilot_skill
        self.weather_conditions = weather_conditions
        self.execution_time =execution_time

    def __repr__(self):
        return (f'Weight:({self.distance}, {self.aircraft_type}, {self.pilot_skill}, '
                f'{self.weather_conditions}, {self.execution_time})\n')