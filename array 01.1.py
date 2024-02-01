array=[11,2,13,14,15,10,12,9,5,7,6]

'''
print(min(array))
print(max(array))

#print max value

array.sort()
print(array[-1])


#print min value

array.sort()
print(array[0])
'''
'''
#Extra
'''
'''
#find the minimum value:
min = array[0]
for i in range(len(array)):
    if array[i]<min:
        min=array[i]
print(min)
'''

#Ass.1 (Q1).
'''
#print max value
print(max(array))
'''
'''
#find maximum value by other method
max=array[0]
for i in range(0,len(array)):
    if array[i]>max:
        max = array[i]
print(max)
'''
#Ass.1 (Q2).

'''
#find the sum of array
sum=0
for i in range(len(array)):
    sum = array[i]+sum
print(sum)

#Ass.1 (Q3).
'''
'''
#find the reverse elements in array
array.reverse()
print(array)
'''
'''
#Ass.1 (Q4).
'''
'''
#array is sorted in ascending order
array.sort()
print(array)
'''

#Ass.1 (Q5).

'''
#count the occurrence of a specific element in an array
i = int(input('Enter the element that you want find out: '))
for n in range(len(array)):
    if array[n]==i:
        print("The value is found",n)
        break
else:
    print("The value is not found")
'''

#Ass.1 (Q3).
'''
for i in range(len(array)-1,-1,-1):
    print(array[i])
'''

#Ass.1 (Q4).

'''
for j in range(0,len(array)-1):
    for i in range(0,len(array)-1):
        m = array[i]
        n = array[i+1]
        if m>n:
            array[i]=n
            array[i+1]=m

print(array)
'''

##(Descending order) reverse sorting another method:
'''
for j in range(0,len(array)-1):
    for i in range(0,len(array)-1):
        if (array[i]<array[i+1]):
            a = array[i]
            array[i]=array[i+1]
            array[i+1]=a
print("reverse sorting: ",array)
'''
'''
print(len(array))
'''
#Ass.1 (Q6)
'''
import numpy as np
ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ar)
#for row major order:
for i in range(len(ar)):
    for j in range(len(ar[i])):
        print("The Traversal of row is ",ar[i][j])

#for column major order:
for j in range(len(ar[0])):
    for i in range(len(ar)):
        print("The Traversal of column is ",ar[i][j])
'''
#Ass. Q7.
'''
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
'''
'''
mx = [[m1[j][i]
       for j in range(len(m1))
       for i in range(len(m1[0]))]]
for i in range(0,len(m1)):
    for j in range(0,len(m1)):
        #b[i][j]=a[j][i]
        print(mx)
for j in range(0,len(m1)):
    for i in range(0, len(m1)):
        print(mx)
'''
'''m2 = [[m1[i][j]
       for i in range(len(m1))
       for j in range(len(m1))]]
       print(m2)
'''

'''
#wrong method
base_add = int(input("Enter the Base Address: "))
w = int(input("Enter the word size in bytes: "))
n = int(input("Enter the number of 'Rows': "))
m = int(input("Enter the number of 'Columns': "))
l1 = int(input("Enter the 'Lower bound of Row': "))
l2 = int(input("Enter the 'Lower bound of Column': "))
#cal for Row major order
cal1 = base_add+w[m(i-l1)+(j-l2)]
print("The Row major Loc: ",cal1)
'''

'''
##Binary search:
a = int(input("Enter the value: "))
for j in range(0,len(array)-1):
   mid = len(array)/2
   b = array[mid]
   print(b)
    if mid<a:
        beg=j+1
        end= array[-1]
        mid=(beg+end)/2
    elif mid>a:
        beg=array[0]
        end=j-1
        mid=(beg+end)/2
    else:
        
print(mid)
'''





#Ass.1 (Q8).
'''
import numpy as np
mat = np.array([[1,0,0],[0,2,0],[0,0,3]])
#mat = np.array([[1,6,0],[5,2,0],[0,4,3]])
print(mat)
num = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat [i][j]==0:
            num +=1

if num>(len(mat)*len(mat[0]))/2:
    print("This is a spare matrix.")
else:
    print("No, This is not spare matrix.")

'''


#Ass.1 Q9.
'''
array = [1,6,2,4,5,8,9,3]
num = int(input("Enter the value: "))
for i in range(len(array)):
    if array[i]==num:
        print("The element",num,"is present at index",i)
        break
    else:
        print("The element",num,"is not present in the array")
'''    

#Ass.1 Q10.
'''
array = [1,12,23,14,5,6,11,13,15,17,19]
for j in range(0,len(array)-1):
    for i in range(0,len(array)-1):
        m = array[i]
        n = array[i+1]
        if m>n:
            array[i]=n
            array[i+1]=m

print(array)


num = int(input("Enter the value: "))

low = 0
high= len(array)-1
#mid= 0

while low<=high:
    mid = (high+low)//2
    if array[mid]==num:
        print("Element is found at index: ",mid)
        break
    elif array[mid]<num:
        low=mid+1

    else:
        high=mid-1
if low>high:
    print("Element is not found")

'''
