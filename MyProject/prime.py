import math
n=int(input("Enter the number: "))
f=1
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        f=0
        break
if f:
    print(n," is a prime number")
else:
    print(n," is not a prime number")