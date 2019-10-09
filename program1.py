from math import *

days = int(input("Please enter the total number of days: "))

def calculatePercentage(pairs, value):
    rate = value / pairs * 100
    rate = round(rate,1)
    return rate



rate1 = 0
rate2 = 0
oldWidget = 0


widgets = []
while True:
    widget = int(input("Please enter a widget: "))
    if widget < 0:
        break
    widgets.append(widget)

day = 1
i = 0
counter = 1
while not counter == days + 1:
    positiveNums = 0
    negativeNums = 0
    pairs = int(ceil((len(widgets) / day)))
    for i in range(pairs):
        try:
            if widgets[i] < widgets[i + counter]:
                positiveNums += 1
            elif widgets[i] > widgets[i + counter]:
                negativeNums += 1

        except IndexError:
            if widgets[i] < widgets[-1]:
                positiveNums += 1
            elif widgets[i] > widgets[-1]:
                negativeNums += 1



    print(pairs,positiveNums,negativeNums)
    rate1 = calculatePercentage(pairs, positiveNums)
    rate2 = calculatePercentage(pairs, negativeNums)
    print("For", day, "day intervals", rate1, "were increasing and", rate2, "were decreasing")
    i = 0
    day += 1
    counter += 1







