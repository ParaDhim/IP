f = open("Admin/RegisteredStudents.txt","r")
readi = f.readlines()
d = {}
for i in readi:
    a = i.strip()
    b = a.split()
    d[b[0]] = b[1]
print(d)
f.close()

for j in d.keys():
    count = 0
    f1 = open(f"Student/{j}_{d[j]}.txt","r")
    k = f1.readlines()
    jkdict = {}
    for jk in k:
        e = jk.strip()
        ee = e.split()
        jkdict[ee[0]] = ee[1]
    f2 = open("Admin/Answerkey.txt","r")
    kk = f2.readlines()
    jkkdict = {}
    for jkk in kk:
        e1 = jkk.strip()
        ee1 = e1.split()
        jkkdict[ee1[0]] = ee1[1]
    f1.close()
    f2.close()
    for check in range(0,len(jkdict)):
        if jkdict[str(check + 1)] == jkkdict[str(check + 1)]:
            count += 4
        elif jkdict[str(check + 1)] == "-":
            count += 0
        elif jkdict[str(check + 1)] != jkkdict[str(check + 1)]:
            count += -1
    f3 = open("Admin/FinalReport.txt","w")
    a =  j + " " + d[j] + " " + str(count) + "\n"
    f3.write(a)
    f3.close()