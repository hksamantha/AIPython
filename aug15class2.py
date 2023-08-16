day = input("Enter a day of the week: ")
match day:
    case "Monday":
        print("Happy", day)
    case "Tuesday":
        print("Happy", day)
    case "Wednesday":
        print("Happy", day)
    case "Thursday":
        print("Happy", day)
    case "Friday":
        print("Happy", day)
    case "Saturday":
        print("Happy", day)
    case "Sunday":
        print("Happy", day)
    case _:
        print("Wrong Input")
