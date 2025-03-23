#removing duplicates from a array using set
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = list(set(arr))
print(arr)

#removing duplicates from a array using loop
res = []
for i in arr:
    if i not in res:
        res.append(i)
print(res)

#removing duplicates from a array using dictionary
res = list(dict.fromkeys(arr))
print(res)

'''Which is Most Efficient?
If you don’t care about preserving order:

Use the set method. It is the fastest and simplest.

If you need to preserve order:

Use the dict.fromkeys() method. It is fast, simple, and preserves order (Python 3.7+).

If you need to preserve order and are working with small arrays:

You can use the loop method, but it is inefficient for large arrays due to its O(n²) time complexity.

Practical Recommendation:
Use set if order doesn’t matter.

Use dict.fromkeys() if order matters.

Avoid the loop method for large arrays due to its inefficiency.'''
