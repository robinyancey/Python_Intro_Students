'''
This takes an integer from
the user and checks if it is prime or not
'''
# Read user input
n = int(input("Please enter an int?"))

# Check if n is a prime
isprime = True
for m in range(2, n):    
    # check if n is divisible by m
    if n % m == 0:
        isprime = False
        break 

# print the result
if isprime:
    print(n, " is a prime number")
else:
    print(n, "is not a prime number")

