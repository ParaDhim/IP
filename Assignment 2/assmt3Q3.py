"""c = input("Enter the value: ")
b1= int(input("Enter the base value need to be changed: "))
b2= int(input("Enter the base value to be given in output: "))
def B1ToDeci(c,b1):
    ans1 = 0
    ans2 = 0
    lst1=[]
    lst2=[]
    for inde in range(0,len(c)):
        if inde < c.index("."):
            lst1.append(c[inde])
        elif inde > c.index("."):
            lst2.append(c[inde])
    print(lst1)
    print(lst2)
    #converting the number to decimal
    for i in range(0,len(lst1)):
        k = (ord(lst1[-1-i]) - 55)
        if k < 3:
            a=int(lst1[-1-i])
            d = a*(b1**i)
            ans1 += d
        elif k > 9:
            d = k*(b1**i)
            ans1 += d
    for i in range(0,len(lst2)):
        k = (ord(lst2[i]) - 55)
        if k < 3:
            a=int(lst2[i])
            d = a*(b1**(-i-1))
            ans2 += d
        elif k > 9:
            d = k*(b1**(-i-1))
            ans2 += d
    return (ans1 + ans2)
b = B1ToDeci("AB12.CB",16)
print(b)"""






# converting decimal no. to b2
"""c = input("Enter the value: ")
b1 = int(input("Enter the base value need to be changed: "))
b2 = int(input("Enter the base value to be given in output: "))"""
def DeciToB2(c,b2):
    lst1 = []
    lst2 = []
    a = ""
    d = ""
    # a = str(c)
    b=[]
    bt=[]
    k = ""
    ap = ""
    dp = ""
    d2 = []
    for inde in range(0,len(c)):
        if inde < c.index("."):
            a = a + (c[inde])
        elif inde > c.index("."):
            d = d + (c[inde])
    a=int(a)
    while a!=0:
        e = a%b2
        if e>9:
            b.insert(0,chr(e+55))
        elif e<9 and e<=36:
            b.insert(0,str(e))
        de = a//b2
        a = de
    for i in range (0,len(b)):
        k=k+str(b[i])
        
    d1 = "0."+d
    di=float(d1)
    for i in range(0,len(d)):
        ap=""
        dp=""
        num = di * b2
        for ind in range(0,len(str(num))):
            if ind < str(num).index("."):
                ap = ap + (str(num)[ind])
            elif ind > str(num).index("."):
                dp = dp + (str(num)[ind])
        if int(ap) >= 10:
            d2.append(chr(int(ap)+55))
        elif int(ap) <= 9:
            d2.append(ap)
        if float(dp) == 0:
            break
        
        di = float("0."+dp)
    alp="."
    for alpha in d2:
        alp = alp + alpha
    return (k+alp)

a=DeciToB2("43794.296875",16)
print(a)

# ---------7) Convert number with radix A to radix B. Here A,B <= 36.
