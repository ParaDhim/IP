from cgi import test
from math import sin,cos
from tkinter import Y

def matmul(A,B):
    ret=[]
    for i in range(len(A)):
        r=[]
        for j in range(len(B[0])):
            temp=0
            for k in range(len(B)):
                temp+=A[i][k]*B[k][j]
            r.append(temp)
        ret.append(r)
    return ret
def rotate(x,y,z,axis,phi):
    cp=cos(phi)
    sp=sin(phi)
    A=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if axis == "x":
        A=[[cp,-sp,0,0],[sp,cp,0,0],[0,0,1,0],[0,0,0,1]]


    elif axis == "y":
        A=[[1,0,0,0],[0,cp,-sp,0],[0,sp,cp,0],[0,0,0,1]]


    elif axis == "z":
        A=[[cp,0,sp,0],[0,1,0,0],[-sp,0,cp,0],[0,0,0,1]]
    for i in range(len(x)):
        ret=matmul(A,[x[i],y[i],z[i],[1]])
        x[i]=ret[0][0]
        y[i]=ret[1][0]
        z[i]=ret[2][0]
    return x,y,z


xx1=[1,2,3,4,5]
yy1=[3,4,5,6,7]
zz1=[3,3,2,4,5]
print(rotate(xx1,yy1,zz1,"x",0.322))