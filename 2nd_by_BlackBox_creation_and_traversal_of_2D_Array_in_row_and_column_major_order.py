def create_2d_array(nrow, ncol, ch):
    ar = []
    for r in range(nrow):
        row = []
        for c in range(ncol):
            if ch == 1:
                a = int(input("Enter Integer number ({},{}) =".format(r, c)))
            elif ch == 2:
                a = str(input("Enter String (Characters) ({},{}) =".format(r, c)))
            elif ch == 3:
                a = float(input("Enter Floating number ({},{}) =".format(r, c)))
            else:
                print("Invalid choice")
                return None
            row.append(a)
        ar.append(row)
    return ar

nrow = int(input("Number of Rows in 2D Array: "))
ncol = int(input("Number of columns in each 2D Array: "))
print("Choose\n1. For write integers\n2. For write String\n3. For write float\n")
ch = int(input("Choose any one option."))

b = create_2d_array(nrow, ncol, ch)
print(b)
