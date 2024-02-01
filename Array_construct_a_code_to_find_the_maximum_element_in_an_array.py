ar=[]
n=int(input("Enter the numbers in the Array "))
for i in range(n):
    a=int(input("Enter number {} = ".format(i+1)))
    ar.append(a)
print("The ARRAY: ",ar)
max=ar[0]
for j in range(0,len(ar)):
    if ar[j]>max:
        max=ar[j]
print(max)

