n=input("Enter the mobile number: ")
s=set(n)
num={'1','2','3','4','5','6','7','8','9','0'}
s = s.symmetric_difference(num)
s=sorted(s)
print("The numbers that are absent in given mobile number are :",s)