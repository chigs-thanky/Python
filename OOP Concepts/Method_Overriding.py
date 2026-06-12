# Method Overriding
# A child class changes the behavior of a parent method.
# Method Overriding
# A child class changes the behavior of a parent method.
class car:
    def start(self): # Class Method
        print("Car engine started!")
    
    def stop(self):
        print("Engine stopped! You can pull out keys!")

class ElectricCar():
    def start(self):
        print("Car motor started!")
        
tata_punch = car()
tata_punch.start()
tata_punch.stop()
tesla = ElectricCar()
tesla.start()
tesla.stop() # AttributeError, that's why inheritance is required.

"""NOTE:Fair point — but "easy" comes at a cost: you lose all the benefits of inheritance. With the second approach (no inheritance), if Car had other methods like stop(), honk(), fuel_type(), etc., ElectricCar wouldn't get any of them. You'd have to rewrite everything from scratch for every new class, even the parts that are identical."""