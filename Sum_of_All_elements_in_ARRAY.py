ar=[]
n=int(input("Enter the numbers in the Array "))
for i in range(n):
    a=int(input("Enter number {} = ".format(i+1)))
    ar.append(a)
print("The ARRAY: ",ar)
sum=0
for j in range(len(ar)):
    sum=ar[i]+sum
print(sum)
