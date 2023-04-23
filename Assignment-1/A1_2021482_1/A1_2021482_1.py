print("Enter 1 for Rignt Angled triangle")
print("Enter 2 for Isosceles triangle")
print("Enter 3 for Kite")
print("Enter 4 for Half Kite")
print("Enter 5 for X")
e = int(input("Enter the value: "))
if e==1:
    n=int(input("ENTER THE VALUE"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
#
elif(e==2):
    if (e%2) == 0:
        c=int(input("Enter the value: "))
        n = c *2
        for i in range(1,n+1,2):
            for k in range(n-i+1,1,-2):
                print("",end=" ")
            for j in range(1,i+1):
                print(j,end="")
            print()
    else:
        print("Wrong Input")
#
elif(e==3):
    if (e%2) == 0:
        c=int(input("Enter the value: "))
        n = c *2
        for i in range(1,n-1,2):
            for k in range(n-i+1,1,-2):
                print("",end=" ")
            for j in range(1,i+1):
                print(j,end="")
            print()
        for l in range(1,n,2):
            for m in range(1,l+1,2):
                print("",end=" ")
            for o in range(1,n-l+1):
                print(o,end="")
            print()
    else:
        print("Wrong Input")

#
elif(e==4):
    n = int(input("ENTER THE VALUE: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    for l in range(1,n+1):
        for o in range(1,n-l+1):
            print(o,end=" ")
        print()

#
elif(e==5):
    if (e%2) == 0:
        c=int(input("Enter the value: "))
        n = c *2
        for l in range(1,n,2):
            for m in range(1,l+1,2):
                print("",end=" ")
            for o in range(1,n-l+1):
                print(o,end="")
            print()
        for i in range(3,n+1,2):
            for k in range(n-i+1,1,-2):
                print("",end=" ")
            for j in range(1,i+1):
                print(j,end="")
            print()
    else:
        print("Wrong Input")

else:
    print("Wrong Input")

