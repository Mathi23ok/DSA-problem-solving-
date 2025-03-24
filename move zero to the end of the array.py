#move all the element to the end of the array
arr = [0, 1, 0, 3, 12]
newa = []
zeroa = []
for i in arr:
    if i != 0:
        newa.append(i)
    else:
        zeroa.append(i)     
newa.extend(zeroa)
print(newa)

#the pythonic approach 
arr = [0, 1, 0, 3, 12,0,13,9]
arr = [x for x in arr if x!=0] + [0]* arr.count(0)
print(arr)

#through index value 
arr = [0, 1, 0, 3, 12,0,13,9]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1
for i in range(j,len(arr)):
    arr[i] = 0
print(arr)

