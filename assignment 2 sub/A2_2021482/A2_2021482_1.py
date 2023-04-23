print("""Enter the Choice:
1. Display specific Word Count
2. Display all Unique Words
3. Display all Word Counts
4. Replace Word
5. Quit
""")

optn = int(input("Enter The Function that you would like to go with: "))
#------1--------
if optn == 1:
    word = input("Enter Word: ")
    f = open("file.txt","r")
    a=[]
    b=[]
    count = 0
    for line in f:
        m = line.split()
        for i in m:
            a.append(i)
        b=b+a
    for i in b:
        if i==word:
            count +=1
    print("Word Count: ",count)
    f.close()
#------1--------

#------2--------
elif optn == 2:
    f = open("file.txt","r")
    a=[]
    b=[]
    c=[]
    for line in f:
        m = line.split()
        for i in m:
            a.append(i)
        b=b+a
    for j in b:
        if j not in c:
            c.append(j)
    for k in c:
        print(k,end=" ; ")
    # c=set(b)
    # for j in c:
    #     print(j,end=" ; ")
    # f.close()

#------2--------

#------3--------
elif optn == 3:
    f = open("file.txt","r")
    a=[]
    b=[]
    c=[]
    for line in f:
        m = line.split()
        for i in m:
            a.append(i)
        b=b+a
    for k in b:
        if k not in c:
            c.append(k)
    print("Word Count: ")
    for j in c:
        count = 0
        for i in b:
            if i==j:
                count +=1
        print(j,":",count)
    f.close()

#------3--------

#------4--------
elif optn == 4:
    wordRep=input("Enter the Word To be replaced: ")
    wordReNeed=input("Enter the Word that you would like to give in replacement of the other: ")
    f=open("file.txt","r")
    data=f.read()
    data=data.replace(wordRep,wordReNeed)
    f.close()
    f=open("file.txt","w")
    f.write(data)
    f.close()

#------4--------


#------5--------

else:
    ("You have Chosen to quit!!")

#------5--------