def noteCreate(lst):
    f1=open("scalemajor.txt","a")
    c = ["W","W","H","W","W","W","H"]
    for j in range(0,12):
        lst1 = []
        start = lst[j]
        lst1.append(start)
        for i in range(0,len(c)):
            if c[i] == "W":
                num2 = lst[(lst.index(start)) + 2]
                lst1.append(num2)
                start = num2
            elif c[i] == "H":
                num3 = lst[(lst.index(start)) + 1]
                lst1.append(num3)
                start = num3
        print(lst1)
        a=""
        for txt in lst1:
            a = a + txt +" "
        f1.write(a)
        f1.write("\n")
    f1.close()

    f2=open("scaleminor.txt","a")
    c1 = ["W","H","W","W","H","W","W"]
    for j1 in range(0,12):
        lst2 = []
        start1 = lst[j1]
        lst2.append(start1)
        for i1 in range(0,len(c1)):
            if c1[i1] == "W":
                num4 = lst[(lst.index(start1)) + 2]
                lst2.append(num4)
                start1 = num4
            elif c1[i1] == "H":
                num5 = lst[(lst.index(start1)) + 1]
                lst2.append(num5)
                start1 = num5
        print(lst2)
        a1=""
        for txt in lst2:
            a1 = a1 + txt +" "
        f2.write(a1)
        f2.write("\n")
    f2.close()

def majorNotes(root):
    f1=open("scalemajor.txt","r")
    for line in f1:
        a = line.split()
        if a[0] == root:
            print(line)
    f1.close()
def minorNotes(root):
    f2=open("scaleminor.txt","r")
    for line in f2:
        a = line.split()
        if a[0] == root:
            print(line)
    f2.close()

lst = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C'"]
noteCreate(lst+lst)
root = input("Enter the Root Note: ")
s = input("Enter the type of scale (Major/Minor): ")
if s == "Major":
    print("The Minor scale in the key of {rn} is: ")
    majorNotes(root)
elif s == "Minor":
    print("The Major scale in the key of {rn} is: ")
    minorNotes(root)
else:
    print("You have chosen the wrong input!!")