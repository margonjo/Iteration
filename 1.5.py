#Marc Gonzalez
#03/11/14
#iteration 1.5
count = 0
total = 0
valid = False

while not valid  :
    number = int(input("please enter a number, when you want the program to end enter -1: "))
    if number == -1:
        valid = True
        average = total / count
        print(average)

    count = count +1
    total = total + number
    

