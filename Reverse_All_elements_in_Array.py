ar=[]
n=int(input("Enter the numbers in the Array "))
for i in range(n):
    a=int(input("Enter number {} = ".format(i+1)))
    ar.append(a)
print("The ARRAY: ",ar)
for j in range(len(ar)-1,-1,-1):
    print(ar[j])
