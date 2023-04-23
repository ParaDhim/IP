from A3_2021482_1 import matmul,scale,translate,rotate
def test_matmul(A,B,C_true):

        assert (C_true==matmul(A,B)),"Test Case Failed "
        return True
def test_scale(x,y,z,sx,sy,sz,Cx_true,Cy_true,Cz_true):
    x1,y1,z1=scale(x,y,z,sx,sy,sz)
    assert(x1==Cx_true and y1==Cy_true and Cz_true==z1),"Test Case Failed "
    return True

def test_translate(x,y,z,tx,ty,tz,Cx_true,Cy_true,Cz_true):
    x1,y1,z1=translate(x,y,z,tx,ty,tz)

    assert(x1==Cx_true and y1==Cy_true and Cz_true==z1),"Test Case Failed "
    return True

def Q1():
    t1=[[[1,2,3],
        [4,6,6],
        [7,8,9]],

        [[3,2,1],
        [4,6,5],
        [8,7,8]],
        [[35,41,35],[80,92,77],[125,143,119]]]
    t2=[[[1,2,3,5],
        [4,5,6,7],
        [7,8,9,3]],

        [[3,2,1],
        [4,6,5],
        [8,9,8],
        [1,1,1]],
        [[40,46,40],[87,99,84],[128,146,122]]
        ]
    t3=[[[1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,5]],

        [[3,2,1,3],
        [4,6,5,5],
        [8,9,8,8]],
        [[35,41,35,37],[80,92,77,85],[125,143,119,133],[59,71,61,63]]]

    tx=[t1,t2,t3]
    print("Test cases for Matmul")
    for i in range(len(tx)): 
        ti=tx[i]
        print(test_matmul(ti[0],ti[1],ti[2]))


    x=[[1,2,3,4,5,6],[4,3,2,1,4,3,2,8]]
    y=[[2,3,4,5,6,7],[3,2,1,4,2,8,1,6]]
    z=[[3,4,5,6,7,8], [8,7,6,5,4,3,2,1]]
    sx=[4,3]
    sy=[2,2]
    sz=[1,2]
    C_x=[[4,8,12,16,20,24],[12,9,6,3,12,9,6,24]]
    C_y=[[4,6,8,10,12,14], [6,4,2,8,4,16,2,12]]
    C_z=[[3,4,5,6,7,8], [16,14,12,10,8,6,4,2]]
    for i in range(2):
        print(test_scale(x[i],y[i],z[i],sx[i],sy[i],sz[i],C_x[i],C_y[i],C_z[i]))
    # test_scale()
    # test_translate()
    # test_rotate()
    x1=[[1,2,3,4,5,6],[4,3,2,1]]
    y1=[[2,3,4,5,6,7],[3,2,1,4]]
    z1=[[3,4,5,6,7,8], [8,7,6,5]]
    tx=[4,3]
    ty=[2,2]
    tz=[1,2]
    cx1=[[5,6,7,8,9,10],[7,6,5,4]]
    cy1=[[4,5,6,7,8,9],[5,4,3,6]]
    cz1=[[4,5,6,7,8,9], [10,9,8,7]]
    for i in range(2):
        test_translate(x1[i],y1[i],z1[i],tx[i],ty[i],tz[i],cx1[i],cy1[i],cz1[i])

    


Q1()