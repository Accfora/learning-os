from garage import Garage
from models.car import Car
from models.truck import Truck
from models.yacht import Yacht

def main():
    c1 = Car("Toyota", "Camry", 2020, 4)
    c2 = Car("Honda", "Civic", 2021, 4)
    t1 = Truck("Volvo", "VNL", 2019, 20000)
    y1 = Yacht("Sunseeker", "Predator 50", 2020, 15, 3)

    print(f"YACHT: {y1.get_info()}")
    print(y1.move())

    g = Garage()
    g.add_vehicle(c1)
    g.add_vehicle(c2)
    g.add_vehicle(t1)
    g.add_vehicle(y1)

    print("\nAll vehicles in the garage:")
    g.show_all()

if __name__ == "__main__":
    main()