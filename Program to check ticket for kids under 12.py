#Program to check ticket for kids under 12 

while True:
    try:
        age = int(input("Enter age of your kid: "))
        break   #exit loop if input is valid
    except ValueError:
        print("Please enter valid age.")

if (age <= 12):
        print("Eligible for free travel.")
else:
        print("Pay for ticket.")