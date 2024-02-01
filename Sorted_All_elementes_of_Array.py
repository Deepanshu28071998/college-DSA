ar=[]
n=int(input("Enter the numbers in the Array "))
for i in range(n):
    a=int(input("Enter number {} = ".format(i+1)))
    ar.append(a)
print("The ARRAY: ",ar)
for j in range(0,len(ar)-1):
    for z in range(0,len(ar)-1):
        m = ar[z]
        n = ar[z+1]
        if m>n:
            ar[z]=n
            ar[z+1]=m

print("Sorted Array is:",ar)
