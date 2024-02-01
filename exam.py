'''
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
'''
'''
c = a+b
print('The sum of both numbers are: ',c)
'''
'''
c = float(input("Enter the third number: "))
if a>b:
    if a>c:
        print(a," is the greatest number.")
    else:
        print(c, " is the greatest number.")
elif b>c:
    print(b," is the greatest number.")
else:
    print(c, "is the greatset number.")
'''
'''
array=[1,2,5,63,85,6,852,54,5,85]
max=array[0]
print(array)
for i in range(len(array)):
    if array[i]>max:
        max=array[i]
print(max," is the greatest number.")
'''
import numpy as np
from scipy.sparse import csr_matrix
sparseMatrix=csr_matrix((3,4))
dtype=np.int(8).toarray()
print(sparseMatrix)


