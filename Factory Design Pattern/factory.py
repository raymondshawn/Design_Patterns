class Car:
    def __init__(self):
        print("Creating a car instance.")

    def drive(self):
        print("Driving the car.")


class Motorcycle:
    def __init__(self):
        print("Creating a motorcycle instance.")

    def ride(self):
        print("Riding the motorcycle.")


class Truck:
    def __init__(self):
        print("Creating a truck instance.")

    def haul(self):
        print("Hauling with the truck.")


def create_vehicle(vehicle_type):
    if vehicle_type == "car":
        return Car()
    elif vehicle_type == "motorcycle":
        return Motorcycle()
    elif vehicle_type == "truck":
        return Truck()
    else:
        raise ValueError("Invalid vehicle type.")
