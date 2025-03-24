#the most efficient way
#finding the intersection and union of two array 
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

if len(arr1) > len(arr2):
    arr1, arr2 = arr2, arr1
set1 = set(arr1)

intersection = []
union = list(arr1)

for x in arr2:
    if x in set1:
        intersection.append(x)
    if x not in set1:
        union.append(x)

print(intersection)
print(union)

#another efficient approach
#finding the intersection and union of two array 
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
arr1 = set(arr1)
arr2 = set(arr2)
intersection = arr1.intersection(arr2)
union = arr1.union(arr2)
print(intersection)
print(union)
