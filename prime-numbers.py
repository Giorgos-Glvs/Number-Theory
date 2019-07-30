
number = int(input("Give an integer number greater than 1: \n"))

while True:
    if number <1: 
        number = int(input("The number should be an integer greater than 1. Try again: \n"))
    else:
        break

def is_number_prime(number):
    '''
    Checks whether a number is prime (returns True) or not (returns False). 
    '''

    is_prime = True
    for i in range(2,number):
        if number%i==0:
            is_prime = False
            break
    return(is_prime)

all_prime_numbers = list() 
for candidate_prime in range(2, number):
    if is_number_prime(candidate_prime):
        all_prime_numbers.append(candidate_prime)

print("Below are all the numbers that are smaller than {} and are primes: ".format(number))
print("\t {}".format(all_prime_numbers))
