def function1(a):
    ## name of the function could be changed
    if a == 1:
        return 1
    else:
        facto = (a * function1(a-1))
    return facto

    pass
def generatedata(num):
    # c = []
    # f=open("testInput.txt","a")
    for i in range(0,num):
        b = int(input())
        f = open(f"testInput{i}.txt","w")
        f.write(str(b))
        f.close()
        f1 = open(f"testInput{i}.txt","r")
        k = f1.read()
        f2 = open(f"testOutput{i}.txt","w")
        f2.write(str(function1(int(k.strip()))))
        f2.close()
        f1.close()


    ## must call function 1
    ## inside it
    pass

num = int(input("Enter the value: "))
generatedata(num)