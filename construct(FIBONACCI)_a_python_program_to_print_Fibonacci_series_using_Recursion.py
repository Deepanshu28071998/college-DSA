n=int(input("Enter the number for fibonacci series: "))
a=0
b=1

if n<1:
    print("No value")
elif n==1:
    print("0")
else:
    print("0\n1")
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c,end="\n")
        
        