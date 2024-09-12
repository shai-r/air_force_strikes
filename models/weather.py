class Weather:

    def __init__(self, city, weather_main, clouds_all, wind_speed):
        self.city = city
        self.weather_main = weather_main
        self.clouds_all = clouds_all
        self.wind_speed = wind_speed

    def __repr__(self):
        return (
            f'Weather:({self.city}, '
            f'{self.weather_main}, '
            f'{self.clouds_all}, '
            f'{self.wind_speed}).\n')