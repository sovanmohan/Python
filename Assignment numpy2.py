import numpy as np
s1=0
arr=np.array([1,2,3,4,5,6,7,8,9])
s2=0
s1=s1+arr[1]+arr[2]+arr[8]
s2=s2+arr[1-len(arr)]+arr[2-len(arr)]+arr[8-len(arr)]
print(s1)
print(s2)
