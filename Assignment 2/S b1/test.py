def re_fibbo(n):
    if n <= 1:
        return n
    else:
        return re_fibbo(n-1) + re_fibbo(n-2)
def testing(n):
    for j in range(n):
        fo = open(f"testInput{j}.txt","r")
        read2 = fo.read()
        fo1 = open(f"testOutput{j}.txt","r")
        read3 = fo1.read()
        if int(read3) == re_fibbo(int(read2)-1):
            print("Success")
        else:
            print("Failed")
        fo.close()
        fo1.close()
        

n = int(input())

testing(n)

