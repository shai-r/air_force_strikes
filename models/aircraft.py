class Aircraft:

    def __init__(self, type, speed, fuel_capacity):
        self.type = type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

    def __repr__(self):
        return f'Aircraft:({self.type}, {self.speed}, {self.fuel_capacity})\n'