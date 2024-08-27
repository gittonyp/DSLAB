str=input()

dicp={}

for i in range(0,len(str)):
    if dicp.get(str[i])==None:
        dicp.update({str[i]:1})
    else:
        dicp.update({str[i]:dicp.get(str[i])+1})

print(dicp)
