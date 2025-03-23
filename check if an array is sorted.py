#to check whether the array is sorted in efficeint way
arr = [12,34,23,45,67,52,98,72]
sort = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sort = False
        break 
if sort:
    print("Array is sorted")
else:   
    print("Array is not sorted")  

#using python inbuilt function, but it is not efficient

sort = arr == sorted(arr)
if sort:
    print("Array is sorted")
else:
    print("Array is not sorted")    
