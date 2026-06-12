class car:
    def __init__(self, B, M, Y):
        self.brand = B
        self.model = M
        self.year = Y

class ElectricCar(car):
    def __init__(self, brand, model, year, battery ):
        super().__init__(brand, model, year)
        self.battery = battery
    
ev = ElectricCar("Tesla","X3","2015","75Kwh")
print(f"{ev.brand} {ev.model} {ev.year} {ev.battery}")
petrol = car("Tata", "Safari", "2025")
print(f"{petrol.brand} {petrol.model} {petrol.year}")