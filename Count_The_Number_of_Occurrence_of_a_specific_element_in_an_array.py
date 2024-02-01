ar=[]
n=int(input("Enter the numbers of elements in Arrya: "))
for i in range(n):
    a=int(input("Enter number {} = ".format(i+1)))
    ar.append(a)
print("The Array:",ar)
a = int(input('Enter the element that you want find out: '))
s=0
while a in ar:
    for j in ar:
        if j==a:
            s=s+1
    print("The value {} is found {} times in this Array.".format(a,s))
    break
else:
    print("The value is not found")
