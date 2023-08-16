class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage, seating_capacity=50):
        super().__init__(name, max_speed, mileage)
        self.default_seating_capacity = seating_capacity

    def seating_capacity(self):
        return super().seating_capacity(self.default_seating_capacity)

autobus = Autobus("Renault Logan", 180, 12)
print(autobus.seating_capacity())
