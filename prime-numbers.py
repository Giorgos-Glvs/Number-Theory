
number = int(input("Give an integer number greater than 1: \n"))

while True:
    if number <1: 
        number = int(input("The number should be an integer greater than 1. Try again: \n"))
    else:
        break

##  Checking if the number is prime: 
is_prime = True
for i in range(2,number):
    if number%i==0:
        is_prime = False
        break

if is_prime:
    print("The number you gave, {}, is a prime number!".format(number))
else:
    print("The number you gave, {}, is not a prime number!".format(number))
