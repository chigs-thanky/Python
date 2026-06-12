class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#class std(): # I forgot to inherit 'student' class, so adding below
class std(student):
    def __init__(self, name, age, std):
        super().__init__(name, age)
        self.std = std
        
eighth = std("Ved", "15", "8th")
print("Name:", eighth.name)
print("Age:", eighth.age)
print("Std:", eighth.std)
    