str=input()
str=str.lower
str=str.split()
dicp={}

for i in str:
    if dicp.get(i)==None:
        dicp.update({i:1})
    else:
        dicp.update({i:dicp.get(i)+1})

print(dicp)
