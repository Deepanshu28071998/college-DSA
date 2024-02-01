#array=[11,12,13,14,15,9,5,10,2,7]
'''
sum=0
for i in range(len(array)):
    sum = array[i]+sum
print(sum)
'''
'''
for i in range(len(array)-1,-1,-1):
    print(array[i])
'''
#practical 5
'''
i = int(input("Enter the element that you want to fuind out: "))
for n in range (len(array)):
    if array[n]==i:
        print("The value is found",n)
        break
    else:
        print("The value is not found")
'''
#practical 6
'''
import numpy as np
ar = np.array([[3,4,5],[6,7,8],[10,11,12]])
print(ar)
for i in range(len(ar)):
    for j in range(len(ar)):
        print(ar[i][j])
for j in range(len(ar)):
    for i in range(len(ar)):
        print(ar[i][j])
'''
