class PetrolCar():
    def fuel_type(self):
        print("Petrol")

class DieselCar:
    def fuel_type(self):
        print("Diesel")

class ElectricCar:
    def fuel_type(self):
        print("Battery")

pc = PetrolCar()
pc.fuel_type()
dc = DieselCar()
dc.fuel_type()
ec = ElectricCar()
ec.fuel_type()


cars = [Car(), ElectricCar()]

for x in cars:
    x.fuel_type()