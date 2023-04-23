f1 = open("Admin//AnswerKey.txt","r")
l = []
lst1 = []
lst2 = []
for line in f1:
    m=line.split()
    lst1.append(m)
# print(lst1)
f1.close()

#opening the registered students file for fetching up the data of students
f2 = open("Admin//RegisteredStudents.txt","r")
for line in f2:
    m1 = line.strip()
    l.append(m1.split())
# print(l)
f2.close()

#Now here we are calculating the marks of the student
lstStu = []
for listNo in range(0,len(l)):
    a1 = l[listNo][0]
    a2 = l[listNo][1]
    # print(a2)
    m2 = f"Student//{a1}_{a2}.txt"
    lstStu.append(m2)
    # print(lstStu)
    
# for stu in range():

for stu in range(0,len(lstStu)):
    f3 = open(lstStu[stu],"r")
    lst3 = []
    for line in f3:
        ls1=line.split()
        lst3.append(ls1)
    # print(lst3)
    count = 0
    for i in range(0,20):
        if  lst3[i][1] == lst1[i][1]:
            count += 4
        elif lst3[i][1] == "-":
            count += 0
        else:
            count += -1
    # print(count)
    f3.close()
    a = str(count)
    #constructing new file and appending data in it for every interation
    f=open("Admin//FinalReport.txt","a")
    f.write(l[stu][0] + l[stu][1] + " " + a + "\n")
    f.close()
    