
number = int(input("Give an integer number greater than 1: \n"))

while True:
    if number <1: 
        number = int(input("The number should be an integer greater than 1. Try again: \n"))
    else:
        break
print("The number you gave is: ".format(number))
print("See you soon!")
