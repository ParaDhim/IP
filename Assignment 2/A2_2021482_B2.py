# gramy = int(input("Enter the number of gramys won till now: "))
# reputation = h * gramy
# 3 Doja dog is going first
# fanville city is m units tall
# has n skyscrapers
# reputation increase by h*gramy
# where 0 represents the sky and a column of 1s is a skyscraper. In the above example, the
# heights of skyscrapers are 2, 3, 4, 1, 5, 3 and 3 respectively
pq = [int(i) for i in input().split()]
P = pq[0]#initial number of Gramys with Doja Dog
Q = pq[1]#initial number of Gramys with DJ Snack
mn = [int(i) for i in input().split()]
repD = 0
repS = 0
m = mn[0]
n = mn[1]
lst1 = []

count = m-1

for i1 in range(0,m):
    lst = [i3 for i3 in input().split()]
    lst2 = []
    for i2 in range(0,len(lst[0])):
        lst2.append(lst[0][i2])
#     if len(lst[0]) == n:
    lst1.append(lst2)
flag =True
for i in range(0,m):
    for j in range (0,len(lst1[0])):
        if flag == True:
            if lst1[i][j] == "1":
                lst1[i][j] = "D"
                flag = not flag
                repD = repD + count * P
                count -= 1
                for j2 in range(0,m):
                    if lst1[j2][j] == "1":
                        lst1[j2][j] = "D"
                # count -= 1
        if flag == False:
            if lst1[i][j] == "1":
                lst1[i][j] = "S"
                flag = not flag
                repS = repS + count * Q
                count -= 1
                for j3 in range(0,m):
                    if lst1[j3][j] == "1":
                        lst1[j3][j] = "S"
    if i != 0:
        P += 1
        Q += 1
#     else:
#         print("PLEASE USE THE SPECIFIC LEnGTH AS EnTERED BY YOU ")
# print(lst1[1][2])
print(repD,repS)
for ij in lst1:
    lstel=""
    for ij1 in range(0,len(ij)):
        lstel = lstel + ij[ij1]
    print(lstel)