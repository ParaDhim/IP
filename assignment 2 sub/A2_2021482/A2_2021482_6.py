print("""
1) Normal traversal( from left to right for each row)
2) Alternating traversal ( first left to right for the first row, then right to left for the second row, then left to right for the third row, and so on.)
3) Spiral traversal from outer to inwards
4) Boundary traversal.(First, traverse the upper boundary from left to right, then rightboundary from up to down, then bottom boundary from right to left and at last from left boundary from down to up)
5) Diagonal traversal from right to left
6) Diagonal traversal from left to right
""")


# 1) Normal traversal( from left to right for each row)
num=int(input("Enter the value: "))
um = int(input("ENTER THE VALUE OF YOUR MATRIX:" ))
if num == 1:
    lst1 = [int(i1) for i1 in input().split()]
    lst = []
    for j1 in lst1:
        lst.append(j1)
    for k1 in range(1,len(lst1)):
        lst2 = [int(l1) for l1 in input().split()]
        for r1 in lst2:
            lst.append(r1)
    print(*lst,sep=" ")
    

# 2) Alternating traversal ( first left to right for the first row, then right to left for the second row,then left to right for the third row, and so on.)

elif num == 2:
    lst1 = [int(i1) for i1 in input().split()]
    lst = []
    for j1 in lst1:
        lst.append(j1)
    for k1 in range(1,len(lst1)):
        lst2 = [int(l1) for l1 in input().split()]
        if k1%2!=0:
            lst2 = lst2[::-1]
            for r1 in lst2:
                lst.append(r1)
        if k1%2==0:
            for r1 in lst2:
                lst.append(r1)
    print(*lst,sep=" ")

# 3) Spiral traversal from outer to inwards
elif num == 3:
    ls1 = []
    ls2 = []
    lst1 = [int(i2) for i2 in input().split()]
    if len(lst1)/2 == 0:
        lst = []
        lstb2 = []
        a1 = {}

        for i1 in lst1:
            lst.append(i1)
        for k1 in range(1,len(lst1)-1):
            lst3 = [int(l1) for l1 in input().split()]
            for k2 in lst3:
                lst.append(k2)
        lst2 = [int(i3) for i3 in input().split()]
        for i4 in lst2:
            lst.append(i4)
        a = len(lst1)
        while a > 0:
            for p in range(0,a):
                ls1.append(lst[p])
            for p1 in range(-1,-(a+1),-1):
                lst.remove(ls1[p1])
            for p2 in range(a-1,len(lst)-a,a):
                ls1.append(lst[p2])
            for p3 in range(-1,-(a-1),-1):
                lst.remove(ls1[p3])
            for p4 in range(-1,-(a+1),-1):
                ls1.append(lst[p4])
            for p5 in range(-1,-(a+1),-1):
                lst.remove(ls1[p5])       
            for p6 in range(-(a-1),-(len(lst)+1),-(a-1)):
                ls1.append(lst[p6])
            for p7 in range(-1,-(a-1),-1):
                lst.remove(ls1[p7])
            a = a - 2
        print(*ls1,sep=" ")
    elif len(lst1)/2 != 0:
        lst = []
        lstb2 = []
        a1 = {}

        for i1 in lst1:
            lst.append(i1)
        for k1 in range(1,len(lst1)-1):
            lst3 = [int(l1) for l1 in input().split()]
            for k2 in lst3:
                lst.append(k2)
        lst2 = [int(i3) for i3 in input().split()]
        for i4 in lst2:
            lst.append(i4)
        a = len(lst1)
        while a > 0:
            for p in range(0,a):
                ls1.append(lst[p])
            for p1 in range(-1,-(a+1),-1):
                lst.remove(ls1[p1])
            for p2 in range(a-1,len(lst)-a,a):
                ls1.append(lst[p2])
            for p3 in range(-1,-(a-1),-1):
                lst.remove(ls1[p3])
            if len(lst) > 1:
                for p4 in range(-1,-(a+1),-1):
                    ls1.append(lst[p4])
                for p5 in range(-1,-(a+1),-1):
                    lst.remove(ls1[p5])       
                for p6 in range(-(a-1),-(len(lst)+1),-(a-1)):
                    ls1.append(lst[p6])
                for p7 in range(-1,-(a-1),-1):
                    lst.remove(ls1[p7])
            elif len(lst) > 1:
                ls1.append(lst[0])
            a = a - 2
        print(*ls1,sep=" ")

    
    

    # for i1 in range(0,lst1):
    #         #we may use not function over here
    #     b=a1[i1+1][-1]
    #     print(lst)
    

    # print(lst1)
    # print(lst)
        
    # print(*lst,sep=" ")

# 4) Boundary traversal.(First, traverse the upper boundary from left to right, then rightboundary from up to down, then bottom boundary from right to left and at last from leftboundary from down to up)

elif num == 4:
    lst1 = [int(i1) for i1 in input().split()]
    lst = []
    lstb2 = []
    for j1 in lst1:
        lst.append(j1)
    for k1 in range(1,len(lst1)-1):
        lst3 = [int(l1) for l1 in input().split()]
        for k2 in lst3:
            lstb2.append(k2)
    lst2 = [int(l1) for l1 in input().split()]

    for i1 in range(len(lst1)-1,len(lstb2),len(lst1)):
        lst.append(lstb2[i1])

    lst2=lst2[::-1]
    for r1 in lst2:
        lst.append(r1)
    for i2 in range(len(lstb2)-len(lst1),-1,-len(lst1)):
        lst.append(lstb2[i2])


    print(lst)
    print(*lst,sep=" ")


# 5) Diagonal traversal from right to left
elif num == 5:
    lst = []
    lsta = []
    lstb = []
    # lst1 = [int(i1) for i1 in input().split()]
    d={}
    d1={}
    dimen = int(input("ENTER THE DIMENSION OF YOUR MATRIX: "))
    for i2 in range(0,dimen):
        a = [int(i3) for i3 in input().split()]
        lst.append(a)
    # b=[i4 for i4 in range(0,dimen)]
    # print(4b)
    # for i in range(0,dimen):
    #     for j in range(0,i):
    for i in range(len(lst)):
        for j in range(i+1):
            print(lst[j][i-j],sep=" ")
        # for k in range():

    for i1 in range(1,len(lst)):
        for k in range(i1,len(lst)):
            print(lst[k][i1-k-1],sep=" ")
# 6) Diagonal traversal from left to right.

elif num == 6:
    lst = []
    lsta = []
    lstb = []
    # lst1 = [int(i1) for i1 in input().split()]
    d={}
    d1={}
    dimen = int(input("ENTER THE DIMENSION OF YOUR MATRIX: "))
    for i2 in range(0,dimen):
        a = [int(i3) for i3 in input().split()]
        lst.append(a)
    # b=[i4 for i4 in range(0,dimen)]
    # print(4b)
    # for i in range(0,dimen):
    #     for j in range(0,i):
    for i in range(0,len(lst)):
        for j in range(0,i+1):
            print(lst[j][j-i-1],sep=" ")
        # for k in range():

    for i1 in range(1,len(lst)):
        for k in range(i1,len(lst)):
            print(lst[k][k-i1],sep=" ")
