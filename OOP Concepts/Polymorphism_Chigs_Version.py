# Combination of Inheritance and Polymorphism
class vehicle:
    def __init__(self, b, m):
        self.brand = b
        self.model = m

class PetrolCar(vehicle):   # vehicle class interited
    def fuel_type(self):
        print(f"{self.brand} {self.model} has fuel type: Petrol")

class DieselCar(vehicle):   # vehicle class interited
    def fuel_type(self):
        print(f"{self.brand} {self.model} has fuel type: Diesel")

class ElectricCar(vehicle): # vehicle class interited
    def fuel_type(self):
        print(f"{self.brand} {self.model} has fuel type: Battery")

pc = PetrolCar("Honda", "City")
pc.fuel_type()
dc = DieselCar("Mahindra", "Thar")
dc.fuel_type()
ec = ElectricCar("Tata", "Nexon")
ec.fuel_type()

print("\nUsing Loop")
cars = [PetrolCar("VolksWagon", "Taigun"), DieselCar("Tata", "Sierra"), ElectricCar("Mahindra", "BE 6")]

for x in cars:
    x.fuel_type()