str=(input("Enter the string: "))
character=(input("Enter the character to be removed: "))
if character in str:
    str=str.replace(character,"")
    print(f"String after removing {character} is {str}")
else:
    print("Character not found in the string")