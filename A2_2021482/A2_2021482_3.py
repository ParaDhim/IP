
# c = input("Enter the value: ")
# b1 = int(input("Enter the base value need to be changed: "))
# b2 = int(input("Enter the base value to be given in output: "))
# c = (input("Enter the value: ")
# b1= int(input("Enter the base value need to be changed: "))
# b2= int(input("Enter the base value to be given in output: "))
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


# converting decimal no. to b2

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


print("""1) Convert decimal to binary and vice-versa
2) Convert decimal to hexadecimal and vice-versa
3) Convert decimal to octal and vice-versa.
4) Convert binary to hexadecimal and vice-versa.
5) Convert binary to octal and vice-versa.
6) Convert hexadecimal to octal and vice-versa.
7) Convert number with radix A to radix B. Here A,B <= 36.
""")

# ---------1) Convert decimal to binary and vice-versa

# ---------1) Convert decimal to binary and vice-versa


# ---------2) Convert decimal to hexadecimal and vice-versa

# ---------2) Convert decimal to hexadecimal and vice-versa
# A=10 B=11 C=12 D=13 E=14 F=15

# ---------3) Convert decimal to octal and vice-versa

# ---------3) Convert decimal to octal and vice-versa


# ---------4) Convert binary to hexadecimal and vice-versa

# ---------4) Convert binary to hexadecimal and vice-versa


# ---------5) Convert binary to octal and vice-versa.

# ---------5) Convert binary to octal and vice-versa.


# ---------6) Convert hexadecimal to octal and vice-versa.

# ---------6) Convert hexadecimal to octal and vice-versa.


# ---------7) Convert number with radix A to radix B. Here A,B <= 36.

# ---------7) Convert number with radix A to radix B. Here A,B <= 36.

oper = int(input("Enter the value for the operation required: "))
if oper == 1:
    oper1 = int(input("""Which type of operation you want to have: 
    1.For B to D
    2. for D to B"""))
    if  oper1 == 1:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a=2
        en1 = B1ToDeci(c,a)
        print(en1)
    if oper1 == 2:
        c = input("Enter the value with decimal value can be .0: ")
        a = 2
        en1 = DeciToB2(c,a)
        print(en1)
    else:
        print("OOPS YOU HAVE CHOSEN THE WRONG INPUT!!")

elif oper==2:
    oper1 = int(input("""Which type of operation you want to have: 
    1.For D to H
    2. for H to D"""))
    if  oper1 == 1:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a=16
        en1 = B1ToDeci(c,a)
        print(en1)
    if oper1 == 2:
        c = input("Enter the value with decimal value can be .0: ")
        a = 16
        en1 = DeciToB2(c,a)
        print(en1)
    else:
        print("OOPS YOU HAVE CHOSEN THE WRONG INPUT!!")

elif oper==3:
    oper1 = int(input("""Which type of operation you want to have: 
    1.For D to O
    2. for O to D"""))
    if  oper1 == 1:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a=8
        en1 = B1ToDeci(c,a)
        print(en1)
    if oper1 == 2:
        c = input("Enter the value with decimal value can be .0: ")
        a = 8
        en1 = DeciToB2(c,a)
        print(en1)
    else:
        print("OOPS YOU HAVE CHOSEN THE WRONG INPUT!!")

elif oper==4:
    oper1 = int(input("""Which type of operation you want to have: 
    1.For B to H
    2. for H to B"""))
    if oper1 == 1:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a=2
        en1 = B1ToDeci(c,a)
        a = 16
        en2 = DeciToB2(str(en1),a)
        print(en2)
    if oper1 == 2:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a = 16
        en1 = B1ToDeci(c,a)
        a = 2
        en2 = DeciToB2(str(en1),a)
        print(en2)

    else:
        print("OOPS YOU HAVE CHOSEN THE WRONG INPUT!!")
elif oper==5:
    oper1 = int(input("""Which type of operation you want to have: 
    1.For B to O
    2. for O to B"""))
    if oper1 == 1:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a=2
        en1 = B1ToDeci(c,a)
        a = 8
        en2 = DeciToB2(str(en1),a)
        print(en2)
    if oper1 == 2:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a = 8
        en1 = B1ToDeci(c,a)
        a = 2
        en2 = DeciToB2(str(en1),a)
        print(en2)

    else:
        print("OOPS YOU HAVE CHOSEN THE WRONG INPUT!!")
elif oper==6:
    oper1 = int(input("""Which type of operation you want to have: 
    1.For H to O
    2. for O to H"""))
    if oper1 == 1:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a=16
        en1 = B1ToDeci(c,a)
        a = 8
        en2 = DeciToB2(str(en1),a)
        print(en2)
    if oper1 == 2:
        c = input("Enter the value with decimal value can be .0: ")
        # for i in a
        a = 8
        en1 = B1ToDeci(c,a)
        a = 16
        en2 = DeciToB2(str(en1),a)
        print(en2)

    else:
        print("OOPS YOU HAVE CHOSEN THE WRONG INPUT!!")
elif oper==7:
    c = input("Enter the value with decimal value can be .0: ")
    # for i in a
    a = int(input("Enter the base value need to be changed: "))
    en1 = B1ToDeci(c,a)
    a = int(input("Enter the base value to be given in output: "))
    en2 = DeciToB2(str(en1),a)
    print(en2)
else:
    print("OOPS YOU HAVE CHOSEN THE WRONG INPUT!!")