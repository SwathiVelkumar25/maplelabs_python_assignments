str=input("Enter the string: ")
revstr="".join(reversed(str))
print(revstr)
if str==revstr:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
