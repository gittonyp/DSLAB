ll = (1, 2, -8, 0)
big = -999999
small=-99999
for i in range(len(ll)):
    if int(ll[i]) > big:
        big = int(ll[i])

for i in range(len(ll)):
    if int(ll[i]) > small and big!=ll[i]:
        small = int(ll[i])

print(big)
print(small)
