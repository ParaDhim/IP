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





# print(lst3)
