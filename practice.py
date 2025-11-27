# x = 10
# y = x * 2 + 5 -3

# for i in range(1, 5):
#     print( i, end=" ")

x = 20

# if x > 10:
#     print("Greater than 10")
# else: 
#     print("10 or less")

# count = 0
# while count < 3:
#     print(count)
#     count += 1

# x = 0

# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x)

# x = 5 
# if x > 2:
#     if x > 4:
#         print("A")
#     else:
#         print("B")
# else:
#     print("C")

# for i in range(1,6):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# total = 0
# for i in range(1,6):
#     total += i
# print(total)

# for x in [1,2,3]:
#     for y in [4,5]:
#         print(x,y)

# x = 0
# for i in range(5):
#     x += i
#     if x > 5:
#         break
#     print(x) 

# count = 0
# while count < 5:
#     if count == 3:
#         break
#     print(count)
#     count += 1

# for i in range(1,4):
#     for j in range(1,i+1):
#         if j%2 ==0:
#             print(i,j)

# for i in range(2,5):
#     for j in range(i):
#         if i % j ==0:
#             print(i,j)

# x = 0
# for i in range(3):
#     for j in range(3):
#         if i + j > 3:
#             x += 1

# print(x)

# for i in range(5):
#     if i ==2:
#         continue
#     for j in range(2):
#         if i == j:
#             break
#         print(i, j)

n = 4
total = 0
for i in range(1, n):
    for j in range(i+1):
        if(i+j)%3==0:
            total+=1
print(total)

# A class
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
# a class method
    @classmethod
    def from_string(cls, vehicle_str):
        make, model, year = vehicle_str.split("-")
        return cls(make, model, year)

# A car class inheriting from vehicle
class Car(Vehicle):

# a class attribute
    vehicle_type = "Car"
    def __init__(self, make, model, year, fuel_capacity, mileage=0):
        super().__init__(make, model, year, mileage)
        self.fuel_capacity = fuel_capacity
    
    def get_info(self):
        return f"{self.make} {self.model}, a {self.year} model with {self._mileage}km mileage and {self.fuel_capacity} L fuel capacity"
    

# inheritance with static method
class ElectricScooter(Vehicle):
    def __init__(self, make, model, year, battery_percentage, mileage=0):
        super().__init__(make, model, year, mileage)
        self.battery_percentage = battery_percentage
    
    def drive(self, distance):
        self.battery_percentage -= distance
        if self.battery_percentage < 0:
            self.battery_percentage = 0
# a method overriding class it is inheriting from
    def get_info(self):
        return f"{self.make} {self.model}, a {self.year} model with {self._mileage}km mileage and {self.battery_percentage}% charge left"
    
    # static method
    @staticmethod
    def is_charging_required(battery_percentage):
        return battery_percentage < 20
    
vehicles = [
    Car("Toyota", "Corolla", 2020, 50),
    ElectricScooter("Xiaomi", "M365", 2022, 85),
    Vehicle.from_string("Honda-Civic-2018")
]


# polymorphism
def print_vehicle_report(vehicles):
    for v in vehicles:
        print(v.get_info())

# calling a polymorphic function
print_vehicle_report(vehicles)

