
number = int(input("Give an integer number: \n"))

while True:
    if number<0:
        number = int(input("The number should be greater than zero. Try again: \n"))
    else:
        break

if number%2==0:
    print("The number {} is even!".format(number))
else:
    print("The number {} is odd!".format(number))

print("Have a nice day! Hope to see you again soon!")
print("This line was added while using GitHub!!")
