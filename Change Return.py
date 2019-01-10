#Change return program
import math

def change_return(change):

    dic = {"quarters": 0, "tens": 0, "fives": 0, "ones": 0}
    counter = 0
    quarters = 25
    tens = 10
    fives = 5
    ones = 1

    if change / quarters >= 0:
        counter = math.floor(change / quarters)
        change -= counter * quarters
        dic["quarters"] = counter
        if change / tens >= 0:
            counter = math.floor(change / tens)
            change -= counter * tens
            dic["tens"] = counter
            if change / fives >= 0:
                counter = math.floor(change / fives)
                change -= counter * fives
                dic["fives"] = counter
                if change / ones >= 0:
                    counter = math.floor(change / ones)
                    change -= counter * ones
                    dic["ones"] = counter


    return dic


amount = int(input("Please enter a amount of money you are giving: "))
cost = int(input("Please enter a cos of item you want to pay: "))
change = amount - cost
print("\nChange what is given to you is: $", change)

quarters = 0
tens = 0
fives = 0
pennies = 0

print()
print(change_return(change))