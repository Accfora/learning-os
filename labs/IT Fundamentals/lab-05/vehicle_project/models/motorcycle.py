from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), has sidecar = {self.has_sidecar}, speed = {self.speed}"

    def move(self):
            return "The motorcycle is moving"