import numpy as np
m1 = np.array([[1,2],
       [3,4],
       [5,6]])
rs = np.array([[0,0,0],[0,0,0]])
print(m1)
print(rs)
for i in range(len(m1)):
    for j in range(len(m1[i])):
        rs[j][i]=m1[i][j]
        
for r in rs:
    print(r)
