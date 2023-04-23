from math import sin,cos,tan
print("""
For scaling, the query looks like:
    --S sx sy sz
where, S represents scaling and sx, sy and sz represent the amount of scale in each axes
For translating, the query looks like:
    --T tx ty tz
where, T represents translation and tx, ty and tz represent the amount of translation in each axes
For rotating, the query looks like:
    --R x 𝝓
""")
# For scaling
n = int(input("Enter the Number of the Vertices: "))
mx = [int(i) for i in input().split()]
my = [int(j) for j in input().split()]
mz = [int(k) for k in input().split()]

mx2 = mx.copy()
my2 = my.copy()
mz2 = mz.copy()
f = open("assmtQ2.txt","a")
a=""

f.write(str(mx)+"\n")
f.write(str(my)+"\n")
f.write(str(mz)+"\n")
f.close()

q = int(input("The number of transformation queries needed to be applied: "))
for query in range(0,q):
    que = [ku for ku in input().split()]
    #----------------1  Scaling----------
    if que[0] == "S":
        sx = int(que[1])
        sy = int(que[2])
        sz = int(que[3])

        for i in range(0,n):
            x = mx[i]
            y = my[i]
            z = mz[i]
            r = 1
            xu = sx*x
            yu = sy*y
            zu = sz*z
            mx[i] = xu
            my[i] = yu
            mz[i] = zu


    #----------------1----------

    #----------------2Translating----------
    elif que[0] == "T":
        tx = int(que[1])
        ty = int(que[2])
        tz = int(que[3])

        for i in range(0,n):
            x = mx[i]
            y = my[i]
            z = mz[i]
            r = 1
            xu = x + tx
            yu = y + ty
            zu = z + tz
            mx[i] = xu
            my[i] = yu
            mz[i] = zu

    #----------------2----------

    #----------------3a Rotation----------
    
    elif que[0] == "R":
        fhi = float(que[2])
        if que[1] == "x":
            for i in range(0,n):
                x = mx[i]
                y = my[i]
                z = mz[i]
                r = 1
                xu = x
                yu = (y*cos(fhi) - z*sin(fhi))
                zu = (y*sin(fhi) + z*cos(fhi))
                mx[i] = xu
                my[i] = yu
                mz[i] = zu

        #----------------3b----------

        elif que[1] == "y":
            for i in range(0,n):
                x = mx[i]
                y = my[i]
                z = mz[i]
                r = 1
                xu = (x*cos(fhi) + z*sin(fhi))
                yu = y
                zu = (z*cos(fhi) - x*sin(fhi))
                mx[i] = xu
                my[i] = yu
                mz[i] = zu

        #----------------3c----------

        elif que[1] == "z":
            for i in range(0,n):
                x = mx[i]
                y = my[i]
                z = mz[i]
                r = 1
                xu = (x*cos(fhi) - y*sin(fhi))
                yu = (x*sin(fhi) + y*cos(fhi))
                zu = z
                mx[i] = xu
                my[i] = yu
                mz[i] = zu
print("The Final transformed 3 lists are: ")

f = open("assmtQ2out.txt","a")
a=""

f.write(str(mx)+"\n")
f.write(str(my)+"\n")
f.write(str(mz)+"\n")
f.close()
print(mx)
print(my)
print(mz)
