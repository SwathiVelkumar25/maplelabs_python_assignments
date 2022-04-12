def rev_dig_palin(n):
  while True:
    num = str(n)
    if num == num[::-1]:
      break
    else:
      rev = int(num[::-1])
      n += rev
  return n

n=int(input("Enter a number between the range 100 and 10000: "))
if (n>=100 and n<=10000):
  print(rev_dig_palin(n))
else:
  print("Number out of range")