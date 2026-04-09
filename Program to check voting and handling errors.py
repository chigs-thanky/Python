#Program to check whether your can vote or not!
try:
    age = int(input("Enter your age: "))

    if (age > 18):
        print("You can vote!")

    else:
        print("You can't vote!")
    
except ValueError:
        print("Invalid Input! Please enter correct details!")