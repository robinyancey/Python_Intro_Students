'''
Our is prime put into a file and input is read from command line
instead of using input()
'''
import sys

# convert it to an int
n = int(sys.argv[1])

is_prime = True

# loop through the numbers 0 to (n - 1)
for m in range(2, n):    
    if n % m == 0:
        is_prime = False
        break
    
print("is ", n, " prime?\t", is_prime) 
