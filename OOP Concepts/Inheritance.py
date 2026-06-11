class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self): # Common method
        print("Car is starting")
    
    def rain_wiper(self): # Common method
        print(f"{self.brand} {self.model} has wiper for rain!")

    def parking(self): # Common method
        print("Parking-Brake applied")

class ElectricCar(Car):
    def charge(self): # Class's Own method
        print("Charging battery")

class PetrolCar(Car):
    def gas(self): # Class's Own method
        print("Filling gasoline")

class dieselCar(Car):
    def gas(self): # Class's Own method
        print("Diesel filling")

# Creating objects
Ecar = ElectricCar("Tesla", "X3") 
Pcar = PetrolCar("Toyota", "Fortuner")
Dcar = dieselCar("Tata", "Harrier")

Ecar.start()   #inherited method from class Car()
Ecar.charge()  # own class method
Ecar.rain_wiper()  #inherited method from class Car()
print("\n")
Pcar.start()  #inherited method from class Car()
Pcar.gas()     # own mclass ethod
Pcar.rain_wiper() #inherited method from class Car()
print("\n")
Dcar.parking() #inherited method from class Car()
Dcar.gas()  # own class method


