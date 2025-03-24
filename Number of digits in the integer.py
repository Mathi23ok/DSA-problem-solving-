#counting the number of digit in the integer
n = int(input("Enter an integer: "))
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print(count)

#another approach 
m = int(input("Enter an integer: "))
print(len(str(m)))
