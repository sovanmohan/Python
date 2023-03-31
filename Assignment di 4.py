import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
newarr=arr[0:24]
for i in newarr:
    print(i)
n1=newarr.reshape(2,12)
for i in n1:
    for j in i:
        print(j)
n2=newarr.reshape(2,3,4)
for i in n2:
    for j in i:
        for k in j:
            print(k)
