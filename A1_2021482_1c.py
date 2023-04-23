#
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
