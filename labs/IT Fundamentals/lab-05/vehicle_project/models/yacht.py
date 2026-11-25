from models.vehicle import Vehicle

class Yacht(Vehicle):
    def __init__(self, brand, model, year, length, cabins):
        super().__init__(brand, model, year)
        self.length = length
        self.cabins = cabins

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}) with length = {self.length} m and {self.cabins} cabins, speed = {self.speed}"

    def move(self):
        if self.speed > 0:
            return "The yacht is moving"
        return "The yacht is not moving"
    