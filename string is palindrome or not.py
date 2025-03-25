#check if a string is a palindrome

s = input("Enter a string: ").lower().replace(" ", "")
if s == s[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

#to check if a string is a palindrome through iteration
s = input("Enter a string: ").lower().replace(" ", "")
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        print("The string is not a palindrome")
        break
    i += 1
    j -= 1

if i >= j:
    print("The string is a palindrome")
