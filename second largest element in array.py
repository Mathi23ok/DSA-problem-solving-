#to find the largest element in the array by iteration 
arr = [12,34,23,45,67,52,98,72]
max = arr[0]
for i in range(len(arr)):
    if max <arr[i]:
        max = arr[i]
smax = arr[0]
for i in range(len(arr)):
    if smax < arr[i] and arr[i] != max:
        smax = arr[i]
print("The largest element in the array is: ",max)
print("The second largest element in the array is: ",smax)

#to find the largest element in the array by using sort() method
arr.sort()
print("The largest element in the array is: ",arr[-2])


#to find the second largest element in the array by traversing the array 
first = second = float('-inf')
for i in range(len(arr)):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif arr[i] > second and arr[i] != first:
        second = arr[i]
print("The second largest element in the array is: ",second)        

'''Iteration Method:

Simple and easy to understand.

Requires two traversals of the array.

sorting :
it is less efficient .

Single Traversal Method:

More efficient for large arrays.

Requires slightly more complex logic.

Choose Based on Context:

Use the iteration method for simplicity and small arrays.

Use the single traversal method for efficiency and large arrays.'''
