#to find the largest element in the array by iteration 
arr = [12,34,23,45,67,52,98,82]
max = arr[0]
for i in range(len(arr)):
    if max <arr[i]:
        max = arr[i]
print("The largest element in the array is: ",max)

#to find the largest element in the array by using sort() method
arr.sort()
print("The largest element in the array is: ",arr[-1])

#to find the largest element in the array by using max() method
print("The largest element in the array is: ",max(arr))

# the time and space complexity of the iteration method is similar , where as sorting will be inefficient , everything works good for small array ,but for a large array max() and iteration will be the best choice 
