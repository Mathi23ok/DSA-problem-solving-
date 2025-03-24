#fatorial of a number 
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Factorial of", n, "is", fact)

#another efficient approach using math module
import math
m = int(input("Enter a number :"))
print(math.factorial(m))
