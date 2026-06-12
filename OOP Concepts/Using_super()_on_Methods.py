class Car:
    def start(self):
        print("Engine Reving...")

class ElectricCar(Car):
    def start(self):
        super().start()
        print("Battery system activated")
        
class PetrolCar(Car):
    def start(self):
        print("Ignition Started! ")
        super().start()

bmw = PetrolCar()
bmw.start()