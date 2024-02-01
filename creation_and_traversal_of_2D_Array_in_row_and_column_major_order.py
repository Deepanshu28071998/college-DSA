row=[]
col=[]
nrow=int(input("Enter the numbers of elements in Row of 2D Array: "))
ncol=int(input("Enter the numbers of elements in Column of 2D Arrya: "))
for i in range(nrow):
    print("ROW:")
    print("Choose\n1. For write integers\n2. For write String\n3. For write float\n")
    ch=int(input("Choose any one option."))
    if ch==1:
        a=int(input("Enter number {} =".format(i+1)))
        row.append(a)
    elif ch==2:
        b=str(input("Enter number {} =".format(i+1)))
        row.append(b)
    elif ch==3:
        c=float(input("Enter number {} =".format(i+1)))
        row.append(c)
    else:
        print("Invalid choice")
for j in range(ncol):
    print("COLUMN")
    print("Choose\n1. For write integers\n2. For write String\n3. For write float\n")
    ch=int(input("Choose any one option."))
    if ch==1:
        a=int(input("Enter number {} =".format(j+1)))
        col.append(a)
    elif ch==2:
        b=str(input("Enter number {} =".format(j+1)))
        col.append(b)
    elif ch==3:
        c=float(input("Enter number {} =".format(j+1)))
        col.append(c)
    else:
        print("Invalid choice")

print("The 2D Array is:",row,col)





'''
import numpy as np
ar = np.array([ar1[],ar2[]])

ar1=[]
ar2=[]
n=int(input("Enter the numbers of elements in Arrya: "))
for i in range(n):
    a=int(input("Enter number {} = ".format(i+1)))
    ar1.append(a)
print("The Array:",ar1)
for row major order:
for i in range(len(ar)):
    for j in range(len(ar[i])):
        print("The Traversal of row is ",ar[i][j])

for column major order:
for j in range(len(ar[0])):
    for i in range(len(ar)):
        print("The Traversal of column is ",ar[i][j])



'''
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
