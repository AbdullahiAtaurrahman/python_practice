class Vehicle:
    def __init__(self, make, model, year, mileage = 0):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage

    def drive(self, distance):
        self._mileage += distance

    def get_info(self):
        return f"{self.make} {self.model} {self.year} model with {self._mileage}km mileage"
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model} Mileage: {self._mileage} km"

    @classmethod
    def from_string(cls, vehicle_str):
        make, model, year = vehicle_str.split("-")
        return cls(make, model, year)

class Car(Vehicle):
    vehicle_type = "Car"
    def __init__(self, make, model, year, fuel_capacity, mileage=0):
        super().__init__(make, model, year, mileage)
        self.fuel_capacity = fuel_capacity
    
    def get_info(self):
        return f"{self.make} {self.model}, a {self.year} model with {self._mileage}km mileage and {self.fuel_capacity} L fuel capacity"
    

class ElectricScooter(Vehicle):
    def __init__(self, make, model, year, battery_percentage, mileage=0):
        super().__init__(make, model, year, mileage)
        self.battery_percentage = battery_percentage
    
    def drive(self, distance):
        self.battery_percentage -= distance
        if self.battery_percentage < 0:
            self.battery_percentage = 0

    def get_info(self):
        return f"{self.make} {self.model}, a {self.year} model with {self._mileage}km mileage and {self.battery_percentage}% charge left"
    
    
    @staticmethod
    def is_charging_required(battery_percentage):
        return battery_percentage < 20
    
vehicles = [
    Car("Toyota", "Corolla", 2020, 50),
    ElectricScooter("Xiaomi", "M365", 2022, 85),
    Vehicle.from_string("Honda-Civic-2018")
]

def print_vehicle_report(vehicles):
    for v in vehicles:
        print(v.get_info())


print_vehicle_report(vehicles)

