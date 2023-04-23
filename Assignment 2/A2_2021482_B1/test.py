## This file must use caes.py
## as well as the function generate data() inside
def function2(n):
    a = 1
    for i in range(1,int(n)+1):
        a = a * i
    return a
    ## this function is simmilar to the function 1 but must be implemented differently
    # pass
def testing(num):
    for i in range(0,num):
        global s
        f = open(f"testInput{i}.txt","r")
        j = f.read()
        m = function2(j)
        f.close()
        f1 = open(f"testOutput{i}.txt","r")
        k = f1.read()
        # f2 = open(f"testOutput{i}.txt","w")
        # f2.write(str(function2(int(k.strip()))))
        # f2.close()
        f1.close()
        if int(k) != m:
            s = "FAILED"
            break
        else:
            s = "SUCCESS"
    if s == "FAILED":
        print(s)
    if s != "FAILED":
        print("SUCCESS")
#     ## This function must useinput output text file pairs generated earlier
#     ##to read the data and test them on the result from function 2
    pass
num = int(input("Enter the value for which you want to check: "))
testing(num)





