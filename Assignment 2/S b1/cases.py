def Fibbo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        first = 0
        second = 1
        for i in range(0,n-2):
            Fibon = first + second
            first = second
            second = Fibon
        return Fibon
        pass

def generatedata(n):
    for j in range(0,n):
        inpu = int(input())
        file1 = open(f"testInput{j}.txt","w+")
        file1.write(str(inpu))
        file1.close()
        file12 = open(f"testInput{j}.txt","r")
        read1 = file12.read()
        file2 = open(f"testOutput{j}.txt","a")
        c = read1.strip()
        print(c)
        func1 = Fibbo(int(c))
        file2.write(str(func1))
        file12.close()

        file2.close()
        pass

n = int(input())
generatedata(n)
