#Marc Gonzalez
#21/10/14
# 2.4 iteration

message = input("please enter your message: ")

length = len(message) - 1
character = ("")
for count in range(length,-1,-1):
    letter = message[count]
    character = character +letter
print(character)
    
