def directions():
    print("\nWelcome to the Running Pace Calculator. Please follow the directions below.")

def userInput():
    validMiles = True
    while validMiles is True:
        try:
            miles = float(input("Enter your mileage: "))
        except ValueError:
            print("Please re-enter a float")
        else:
            time = input("Enter your time in the format hh/mm/ss (i.e 02:35:16): ")
            checkedMiles, checkedTime = checkValidity(miles, time)
            break
    return checkedMiles, checkedTime

def checkValidity(miles, time):
    bad = True
    while bad is True:
        if (miles < 0) or (len(time) != 8):
            print("\nEither mileage or time is invalid - try again")
            miles, time = userInput()
        else:
            break
    return miles, time
            
def calculation():
    miles, time = userInput()
    hours = int(time[0:2])
    minutes = int(time[3:5])
    seconds = int(time[6:8])
    hours *= 3600
    minutes *= 60
    sum = hours + minutes + seconds
    standardPace = sum/miles
    minutePace = int(standardPace) // 60
    secondPace = standardPace - (minutePace * 60)
    if secondPace < 10:
        secondPace = f'0{round(secondPace)}'
    result = f"Your pace is {minutePace}:{secondPace} per mile. \n"
    return result

def logic():
    directions()
    print(calculation())

def main():
    logic()
    doAgain = True
    while doAgain is True:
        x = input("Do you want to use the application again? (enter y/n): ")
        if x == "y":
            logic()
        else:
            print("Thanks for using")
            break

main()