print("This program will output the average, max, and min of any given positive numbers.")
print("You can stop the input of numbers by inputting any negative number.")
run = True

#asks user if they want to try again
def reRun():
    run = True
    response = input("would you like to try again? (yes or no): ")
    if response.lower() == "no":
        print("Thank you for using this program")
        run = False
        return run
    print("----------------------------------------------")
    return run

#gets all the numbers the user wants to calculates
def getNumbers():
    inputs = 0
    tSum = 0
    max = 0
    min = 10000000000000000
    while True:
        numString = input("Please enter a number: ")
        checkNegativeNum = numString.lstrip("-")
        if not checkNegativeNum.isdigit():
            print("Please make you sure you enter a valid number")
            continue
        else:
            num1 = float(numString)
        if inputs == 0 and num1 < 0:
           print("Please input numbers to compute an average, max, and min")
           continue
        elif num1 < 0:
            break
        else:
            tSum = num1 + tSum
            inputs = inputs + 1
            if num1 > max:
                max = num1
            if num1 < min:
                min = num1
    return tSum,inputs,max,min

#calculates the average from the inputs
def calculateAvg(tSum,inputs):
    average = tSum / inputs
    return average

#prints the values
def printValues(average, max, min):
    print("The average of these values are", average)
    print("The maximum of your values is", max)
    print("The minimum of your values is", min)

#calls on methods to run program
while run:
    tSum, inputs, max, min = getNumbers()
    average = calculateAvg(tSum,inputs)
    printValues(average, max, min)
    run = reRun()
