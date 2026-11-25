from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0

    @abstractmethod
    def move(self):
        pass

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative")
        self._speed = value

    def accelerate(self, value):
        self.speed += value

    def brake(self, value):
        self.speed -= value

    def stop(self):
        self._speed = 0

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), speed = {self.speed}"

    def __str__(self):
        return self.get_info()
    