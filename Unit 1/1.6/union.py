def inter(ll,ll2):
    for i in range(len(ll)):
        fl=0
        for j in range(len(ll2)):
            if ll2[j]==ll[i]:
                fl=1
        if fl==1:
            print(ll[i])

def union(ll,ll2):
    ll.append(ll2)
    print(ll)
ll=[1,10,156,74,13,19,56]
ll2=[1,156,13,56,77,966,138]

union(ll,ll2)