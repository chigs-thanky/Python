class car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.__engine = "Turbo-V8" # Private attribute (Encapsulation) This attribute cannot directly accessed, accessed only through methods
    
    def engineType(self):
        print(self.__engine)
        # Improved print
        print(f"{self.brand} {self.model} has {self.__engine} engine!")
        
    def accelerate(self):
        self.speed += 20
        print(f"Speed of {self.brand} {self.model} after acceleration: {self.speed} kmph")
        
    def show_speed(self):
        print(f"Speed of {self.brand} {self.model} initially: {self.speed} kmph")
        
vwt = car("Volkswagon", "Taigun", 50)
vwt.show_speed()
vwt.accelerate()
vwt.accelerate()
print("")
tp = car("Tata", "Punch", 40)
tp.show_speed()
tp.accelerate()
tp.accelerate()
tp.accelerate()
print("")
tp.engineType()
vwt.engineType()
