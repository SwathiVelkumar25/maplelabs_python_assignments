def no_of_zeros(n):
    t=0
    while(n/5 > 0):
        t+=(n/5)
        n/=5
    return int(t)
n=int(input("Enter the number: "))
print(no_of_zeros(n))
