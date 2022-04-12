str=(input("Enter the string: "))
occ={}
for x in str:
    if x in occ:
        occ[x]+=1
    else:
        occ[x]=1
print(occ)
cha=(input("Enter character: "))
if cha in occ:
    print(f"The occurence of {cha} is: ",occ[cha])
else:
    print("Character not found in the given string")
