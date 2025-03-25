#reverse a string using iteration
s = input("Enter a string: ")
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print()
#but this is not a efficient way to reverse a string

#we can use slicing to reverse a string
print(s[::-1])

#or we can use reversed() function
print(''.join(reversed(s)))

#or we can use recursion
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
