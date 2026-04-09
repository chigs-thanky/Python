#Program to match-case statements

# day = int(input("Enter the day of week: ")) #For taking number input
day = input("Enter day: ").strip().lower()
    
if day.isdigit():
        print("Invalid Input")

else:
    match day:
        case "monday":
            print("Start of the week!")
        case "friday":
            print("Weekend is near!")
        case 'saturday' | 'sunday': #multiple matches
            print("It's weekend!")
        case _:
            print("Just a regular day!")
        