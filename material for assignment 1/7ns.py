def fxn(x,l):
    eqna=0
    for j in l:
        eqn = x**j
        eqna += eqn
    return(eqna)

def calculate_area(l,a,b,d):
    # def f(x,l):
    #     eqn=0
    #     for j in l:
    #         eqn = x**j
    #         eqn += eqn
    answ = 0
    for i in range(a,b,d):
        if (b-a)%d == 0:
            prev = i
            pres = i + d
            ans = (((pres-prev)/6)*(fxn(prev,l)+(4*fxn(((pres+prev)/2),l))+fxn(pres,l)))
            answ = answ + ans
        else:
            print("exited")
            return 0
            break
    print(int(answ))
            
c=input("enter the value by providing space between them:")
a = int(input("Enter the value of initial range a: "))
b = int(input("Enter the value of final range b: "))
d = int(input("Enter the common difference: "))

sp=c.split(" ")
l=[]
for s in range (0,len(sp)):
    l.append(int(sp[s]))
# print(l)
calculate_area(l,a,b,d)

    