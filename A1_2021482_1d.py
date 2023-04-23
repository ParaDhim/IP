#
n = int(input("ENTER THE VALUE: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for l in range(1,n+1):
    for o in range(1,n-l+1):
        print(o,end=" ")
    print()