class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
class Manager(Employee):
    def __init__(self, name,email, salary):
        super().__init__(name, email)
        self.salary = salary

class CEO(Employee):
    def __init__(self, name, email, position):
        super().__init__(name, email)
        self.position = position

manager = Manager("Chigs", "chigs@gmail.com","25000")
print(f"Name: {manager.name}")
print(f"Email: {manager.email}")
print(f"Salary: Rs.{manager.salary}/m")

ceo = CEO("Chiku", "chiku@gmail.com", "Chief Execute Officer")
print(f"{ceo.name} is our new {ceo.position} and his contact is '{ceo.email}'.")