import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
newarr=arr[0:24]
newarr=arr[0:24]
for i in np.nditer(newarr):
    print(i)
n1=newarr.reshape(2,12)
for i in np.nditer(n1):
        print(i)
n2=newarr.reshape(2,3,4)
for i in np.nditer(n2):
    print(i)
