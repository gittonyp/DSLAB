import numpy as np

a=[[2,1,3,5],
[0,5,2,7],
[1,1,2,9]]
b=[[1]*3]*4

a=np.array(a)
b=np.array(b)
c=np.matmul(a,b)
print(c)

