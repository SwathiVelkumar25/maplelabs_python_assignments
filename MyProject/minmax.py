n=int(input("enter the size of the array: "))
a=[]
for i in range(n):
    x=int(input(f"enter {i+1}th element: "))
    a.append(x)
mini=a[0]
maxi=a[0]
for i in a:
    mini=min(i,mini)
    maxi=max(i,maxi)
print(f"Maximum is {maxi} and minimum is {mini}")