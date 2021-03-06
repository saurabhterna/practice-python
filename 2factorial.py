"""
import time
start_time = time.time()
num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

print("--- %s seconds ---" % (time.time() - start_time))

"""
# USING RECURSION FOR FACTORIAL CALCULATION
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

# Change this value for a different result
num = 8

# uncomment to take input from the user
#num = int(input("Enter a number: "))

# check is the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))
