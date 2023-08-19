class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

transport = Transport("Renault Logan", 180, 12)
print(f"Название транспорта: {transport.name} Скорость: {transport.max_speed} Пробег: {transport.mileage}")
