nrow=int(input("Number of Rows in 2D Array: "))
ncol=int(input("Number of columns in each 2D Array: "))
print("Choose\n1. For write integers\n2. For write String\n3. For write float\n")
ch=int(input("Choose any one option."))
b=[]
d=[]
#ar=[]

for r in range(nrow):
    ar=[]
    for c in range(ncol):
        if ch==1:
            a=int(input("Enter Integer number ({},{}) =".format(r,c)))
        
        elif ch==2:
            a=str(input("Enter String (Characters) ({},{}) =".format(r,c)))
                #row.append(b)
        elif ch==3:
            a=float(input("Enter Floating number ({},{}) =".format(r,c)))
                #row.append(c)
        else:
            print("Invalid choice")
        ar.append(a)
    #print(ar)
    d.append(ar)
#b.append(d)
print(d)






'''
row=[]
col=[]
nrow=int(input("Enter the numbers of elements in Row of 2D Array: "))
ncol=int(input("Enter the numbers of elements in Column of 2D Arrya: "))

print("ROW:")
print("Choose\n1. For write integers\n2. For write String\n3. For write float\n")
ch=int(input("Choose any one option."))

for i in range(nrow):
    if ch==1:
        a=int(input("Enter Integer number {} =".format(i+1)))
        
    elif ch==2:
        a=str(input("Enter String (Characters) {} =".format(i+1)))
            #row.append(b)
    elif ch==3:
        a=float(input("Enter Floating number {} =".format(i+1)))
            #row.append(c)
    else:
        print("Invalid choice")
    row.append(a)




print("COLUMN")
#print("Choose\n1. For write integers\n2. For write String\n3. For write float\n")
#ch=int(input("Choose any one option."))

for j in range(ncol):
    
    if ch==1:
        b=int(input("Enter Integer number {} =".format(j+1)))
            
    elif ch==2:
        b=str(input("Enter String (Characters) {} =".format(j+1)))
            #col.append(b)
    elif ch==3:
        b=float(input("Enter Floating number {} =".format(j+1)))
            #col.append(c)
    else:
        print("Invalid choice")

    col.append(b)
print("The 2D Array is:",row,col)

'''
