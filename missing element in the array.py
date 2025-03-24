#finding the missing element of the array 
arr = [1,2,3,4,6,7,8,9,10]
sum = 0
l = arr[-1]
n = int( l*(l+1)/2)
for i in arr:
    sum += i
print(n-sum)
