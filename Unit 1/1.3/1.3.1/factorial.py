def fact(n):
    if n==1:
        return 1;
    return n*fact(n-1)
i=int(input())
print(fact(i))