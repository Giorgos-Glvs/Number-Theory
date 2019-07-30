##  The script asks a number from the user, and prints all the numbers smaller than this number that are primes: 

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

##  Ask for user input:
number = int(input("Give an integer number greater than 1: \n"))
while True:
    if number <1: 
        number = int(input("The number should be an integer greater than 1. Try again: \n"))
    else:
        break

##  Store all the prime numbers in a list:        
all_prime_numbers = list() 
for candidate_prime in range(2, number):
    if is_number_prime(candidate_prime):
        all_prime_numbers.append(candidate_prime)

##  Print the output:        
print("Below are all the numbers that are smaller than {} and are primes: ".format(number))
print("\t {}".format(all_prime_numbers))
