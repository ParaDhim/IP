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
"""if num == 1:
    lst1 = [int(i1) for i1 in input().split()]
    lst = []
    for j1 in lst1:
        lst.append(j1)
    for k1 in range(1,len(lst1)):
        lst2 = [int(l1) for l1 in input().split()]
        for r1 in lst2:
            lst.append(r1)
    print(*lst,sep=" ")"""
    

# 2) Alternating traversal ( first left to right for the first row, then right to left for the second row,then left to right for the third row, and so on.)

"""if num == 2:
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
    print(*lst,sep=" ")"""

# 3) Spiral traversal from outer to inwards
"""if num == 3:
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
        print(*ls1,sep=" ")"""

    
    

"""for i1 in range(0,lst1):
        #we may use not function over here
        b=a1[i+1][-1]
    print(lst)"""
    

    # print(lst1)
    # print(lst)
        
    # print(*lst,sep=" ")

# 4) Boundary traversal.(First, traverse the upper boundary from left to right, then rightboundary from up to down, then bottom boundary from right to left and at last from leftboundary from down to up)

"""if num == 4:
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
    print(*lst,sep=" ")"""


# 5) Diagonal traversal from right to left
if num == 5:
    lst = []
    lsta = []
    lstb = []
    lst1 = [int(i1) for i1 in input().split()]
    d={}
    d1={}
    for j in range(0,len(lst1)):
        lst.append(lst1[j])
    d[0] = lst1
    for i2 in range(1,len(lst1)):
        lst2 = [int(i1) for i1 in input().split()]
        for k2 in range (0,len(lst2)):
            lst.append(lst2[k2])
            d[i2] = lst2
    for i3 in range(0,len(d)):
        for i4 in range (0,len(d[i3])):
            lstb.append(d[i3][i4])
        # if lst[i] not
        # lsta.append(lst)
    for p1 in range(0,len(lst1)):
        lstc = []
        for p2 in range(p1,len(lstb),len(lst1)):
            lstc.append(lstb[p2])
        d1[p1]=lstc
    print(d1)
    for j in range(0,len(d)):
        # for i in range (0,len(d)): 
        #     # lsta.append(d[j][i])
        #     if i == j:
        #         lsta.append(d[j][j])
            # if d[j][i] not in lsta:
            #     lsta.append(d[i][j])
            for i in range(0,j+1):
                if d[i][j] not in lsta:
                    lsta.append(d[i][j])
                    for p in range(0,i+2):
                        if d[j][i] not in lsta:
                            lsta.append(d[j][i])
        # for i in range(0,j):

    print(lsta)
    
    
    # print(lst3)



# 6) Diagonal traversal from left to right.


