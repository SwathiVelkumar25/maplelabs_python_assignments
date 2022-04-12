str=input("Enter the string: ")
v=['a','e','i','o','u']
vowel={}
cons={}
for x in str:
    if x in v:
        if x in vowel:
            vowel[x]+=1
        else:
            vowel[x]=1
    else:
        if x in cons:
            cons[x]+=1
        else:
            cons[x]=1
print("Vowel occurence: ",vowel)
print("Consonants occurence ",cons)
