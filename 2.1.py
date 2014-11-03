#Marc Gonzalez
#03/11/14
#iteration 2.1

number_1 = int(input("please enter your value for n!: "))
total= 1
previous = 1

number = number_1 + 1
for count in range(1,number):
    
    total = total * count
print(total)
