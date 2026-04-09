#Program to check seniority
age = int(input("Enter your age: "))

if age >= 60:
    user_input = input("Are you member? Yes or No: ").strip().lower()
    if user_input == "yes" or user_input == "y":
        print("50% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")