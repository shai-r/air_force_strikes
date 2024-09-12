class Location:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f'Location:({self.lat}, {self.lon})\n'