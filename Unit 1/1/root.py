import math
n=int(input("Enter "))
flag=0
for i in range(2,math.sqrt(n)+1):
    if n%i==0:
      flag=1

if flag==0:
    print("Prime")
else:
    print("Not Prime")