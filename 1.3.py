#Marc Gonzalez
#01/11/14
#iteration 1.3

amount = int(input("Please enter the amount of numbers you want to be averaged: "))
total = 0
for count in range(amount):
    number = int(input("please enter a numer: "))
    total = total + number
average = total / amount

print(average)
