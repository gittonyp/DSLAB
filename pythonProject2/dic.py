ll = (1, 2, -8, 0)
ll2 = ("a", "b", "C", "d")

di={}

for i in range(0,len(ll)):
    di.update({ll[i]:ll2[i]})

print(di)