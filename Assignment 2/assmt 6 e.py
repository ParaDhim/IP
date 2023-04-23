um = int(input("Enter the dimesion of the matrix: "))
lst = []
for i1 in range(0,um):
    a = [int(j1) for j1 in input().split()]
    lst.append(a)
"""for i in range(0,len(lst)):
    for j in range(0,i+1):
        print(lst[i][j-i])"""
for i in range(0,len(lst)):
    for j in range(0,i+1):
        print(lst[j][j-i],sep=" ")



