
# program to prompt for 8 numbers and report the total to the user

counter = 1
total = 0

while counter < 9 :
    num  = int(input("Enter number{0}: ".format(counter)))
    total = num + total 
    counter = counter + 1
print(total)












