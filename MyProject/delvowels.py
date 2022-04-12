str=input("Enter the string: ")
v=['a','e','i','o','u']
for x in str:
    if x in v:
        str=str.replace(x,"")
print("String after deleting vowels: ",str)