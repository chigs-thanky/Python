class Human:
    # Define Class Properties
    def __init__(self, n, g, o):
        self.name = n
        self.gender = g
        self.occupation = o

    # Define Class Methods
    def do_work(self): #1st method
        if self.occupation == "Tennis Player":
            print(f"{self.name} plays Tennis")
        elif self.occupation == "Actor":
            print(f"{self.name} shoots movies")

    def speaks(self): #2nd method
        print(f"{self.name} says 'How are you?'")

tom = Human("Tom Cruise", "Male", "Actor")
tom.do_work()
tom.speaks()