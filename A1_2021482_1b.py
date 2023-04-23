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
    