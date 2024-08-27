from test_pycosat import nvars1

n=0
n2=1

for i in range(0,10):
    print(n)
    temp=n
    n = n2
    n2=temp+n2
