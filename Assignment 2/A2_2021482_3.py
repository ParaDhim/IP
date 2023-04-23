##need to do the decimal thing#####
# ---------1) Convert decimal to binary and vice-versa



"""def DeciToBin(a):
    b=[]
    k=""
    while a!=0:
        c = a%2
        d = a//2
        b.insert(0,c)
        a = d
    for i in range (0,len(b)):
        k=k+str(b[i])
    return int(k)


def BinToDeci(a):
    c=0
    for i in range(0,len(str(a))):
        b = a%10
        d = b*(2**i)
        c += d
        a = a//10
    return c

# ---------1) Convert decimal to binary and vice-versa

# ---------2) Convert decimal to hexadecimal and vice-versa
# A=10 B=11 C=12 D=13 E=14 F=15
def HexToDeci(a):
    c=0
    for i in range(0,len(str(a))):
        b = a%10
        d = b*(16**i)
        c += d
        a = a//10
    return c

# ---------2) Convert decimal to hexadecimal and vice-versa

# ---------3) Convert decimal to octal and vice-versa

def DeciToOct(a):
    b=[]
    k=""
    while a!=0:
        c = a%8
        d = a//8
        b.insert(0,c)
        a = d
    for i in range (0,len(b)):
        k=k+str(b[i])
    return int(k)

def OctToDeci(a):
    c=0
    for i in range(0,len(str(a))):
        b = a%10
        d = b*(8**i)
        c += d
        a = a//10
    return c"""

# ---------3) Convert decimal to octal and vice-versa

# ---------4) Convert binary to hexadecimal and vice-versa



# ---------4) Convert binary to hexadecimal and vice-versa

# ---------5) Convert binary to octal and vice-versa.



# ---------5) Convert binary to octal and vice-versa.

# ---------6) Convert hexadecimal to octal and vice-versa.



# ---------6) Convert hexadecimal to octal and vice-versa.

# ---------7) Convert number with radix A to radix B. Here A,B <= 36.

"""c = input("Enter the value: ")
b1= int(input("Enter the base value need to be changed: "))
b2= int(input("Enter the base value to be given in output: "))"""
def B1ToDeci(c,b1):
    ans = 0
    lst1=[]
    lst2=[]
    for inde in range(0,len(c)):
        if inde < c.index("."):
            lst1.append(c[inde])
        elif inde > c.index("."):
            lst2.append(c[inde])
    print(lst1)
    print(lst2)
#     for i in range(0,len(c)):
#         lst.append(c[i])
#     print(lst)
#     #converting the number to decimal
#     for i in range(0,len(lst)):
#         k = (ord(lst[-1-i]) - 55)
#         if k < 3:
#             a=int(lst[-1-i])
#             d = a*(b1**i)
#             ans += d
#         elif k > 9:
#             d = k*(b1**i)
#             ans1 += d

B1ToDeci("AB12.CB",16)
# # converting decimal no. to b2
# """c = input("Enter the value: ")
# b1 = int(input("Enter the base value need to be changed: "))
# b2 = int(input("Enter the base value to be given in output: "))"""
# def DeciToB2(c,b2):
#     bt = int(c)
#     b=[]
#     k=""
#     while bt!=0:
#         e = bt%b2
#         if e>9:
#             b.insert(0,chr(e+55))
#         elif e<9 and e<=36:
#             b.insert(0,str(e))
#         d = bt//b2
#         bt = d
#     for i in range (0,len(b)):
#         k=k+str(b[i])
#     print(k)


# ---------7) Convert number with radix A to radix B. Here A,B <= 36.