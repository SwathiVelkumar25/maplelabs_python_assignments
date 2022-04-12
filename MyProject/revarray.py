n=int(input("size of the array: "))
arr=[]
ans=[]
for i in range(n):
    x=int(input(f"\nenter {i+1}th element: "))
    arr.append(x)
n=n-1
while n>=0:
    print(arr[n])
    n-=1