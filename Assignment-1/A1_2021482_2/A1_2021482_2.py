n=int(input("For how many students you want to run this program: "))
for i in range (1,n+1):
    print("------------------------MENU-------------------------------")
    shap = """Choose your Shape
    1.Square
    2.Rectangle
    3.Rhombus
    4.Parallelogram
    5.Circle input
    6.Cube input
    7.Cuboid input
    8.Right Circular cone
    9.Hemisphere Input
    10.Sphere Input
    11.Solid Cylinder
    12.Hollow Cylinder
    13.Exit"""
    print(shap)
    num = int(input("ENTER THE VALUE: "))
    if (num == 1):
        s = int(input("Enter the side of the square: "))
        print("The Perimeter of the square is",4*s)
        print("The Area of the square is",s*s)
    elif (num == 2):
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the width of the rectangle: "))
        print("The Perimeter of the rectangle is",(2*(width + height)))
        print("The Area of the rectangle is",(width * height))
    elif (num == 3):
        rside = int(input("Enter the side of Rhombus: "))
        d1 = int(input("Enter the first diagnal of Rhombus: "))
        d2 = int(input("Enter the second diagnal of Rhombus: "))
        print("The Perimeter of the Rhombus is",(4*rside))
        print("The Area of the Rhombus is",((d1 * d2)/2))
    elif (num == 4):
        b1 = int(input("Enter the value of 1st parallel side: "))
        b2 = int(input("Enter the value of 2nd parallel side: "))
        a = int(input("Enter the value of non-paralled side: "))
        c = int(input("Enter the value of other non-parallel side: "))
        c = int(input("Enter the value of height of the trapezium: "))
        print("The Perimeter of the Trapezium is",(a + b1 + b2 + c))
        print("The Area of the Trapezium is",(0.5 * (b1 + b2) * h))
    elif (num == 5):
        r = int(input("Enter the radius of the circle: "))
        print("The Circumference of the Circle is",(2 * (22/7) * r))
        print("The Area of the Circle is",((22/7) * ((r)**2)))
    elif (num == 6):
        csi = int(input("Enter the side of the cube :"))
        print("The of CSA of the cube :",4*(s**2))
        print("The of TSA of the cube :",6*(s**2))
        print("The of Volume of the cube :",s**3)
    elif (num == 7):
        le = int(input("Enter the length of the cuboid :"))
        br = int(input("Enter the breath of the cuboid :"))
        he = int(input("Enter the height of the cuboid :"))
        print("The of CSA of the cuboid :",2*he*(le + br))
        print("The of TSA of the cuboid :",2 * ((le*br)+(br*he)+(le*he)))
        print("The of Volume of the cuboid :",le*br*he)
    elif (num == 8):
        sh = int(input("Enter the slant height of Right Circular cone: "))
        r = int(input("Enter the radius of Right Circular cone: "))
        h = int(input("Enter the height of Right Circular cone: "))
        s = (((r**2)+(h**2))*0.5)
        print("The of CSA of the Right Circular cone :",(22/7)*r*s)
        print("The of TSA of the Right Circular cone :",(((22/7)*(r**2)) + (22/7)*r*s))
        print("The of Volume of the Right Circular cone :",(1/3)*(22/7)*(r**2)*h)
    elif (num == 9):
        r = int(input("Enter the radius of Hemisphere: "))
        print("The of CSA of the Hemisphere :",2*(22/7)*(r**2))
        print("The of TSA of the Hemisphere :",(3*(22/7)*(r**2)))
        print("The of Volume of the Hemisphere :",((2/3)*(22/7)*(r**3)))
    elif (num == 10):
        r = int(input("Enter the radius of Sphere: "))
        print("The of TSA of the Sphere :",(4*(22/7)*(r**2)))
        print("The of Volume of the Sphere :",((4/3)*(22/7)*(r**3)))
    elif (num == 11):
        r = int(input("Enter the radius of Solid Cylinder: "))
        h = int(input("Enter the height of the Solid Cylinder: "))
        print("The of CSA of the Solid Cylinder :",2*(22/7)*(r)*(h))
        print("The of TSA of the Solid Cylinder :",2*(22/7)*(r)*(r + h))
        print("The of Volume of the Solid Cylinder :",((22/7)*(r**2)*(h)))
    elif (num == 12):
        r1 = int(input("Enter the radius of Hollow Cylinder inner one: "))
        r2 = int(input("Enter the radius of Hollow Cylinder outer one: "))
        h = int(input("Enter the height of the Hollow Cylinder: "))
        print("The of CSA of the Hollow Cylinder :",(2*(22/7)*h*(r2 + r1)))
        print("The of TSA of the Hollow Cylinder :",(2*(22/7)*h*(r2 + r1)) + (2*(22/7)*((r2 ** 2)-(r1 ** 2))))
        print("The of Volume of the Hollow Cylinder :",((22/7)*((r2 ** 2)-(r1 ** 2))*h))
    elif (num == 13):
        break
    else:
        print("Err You have entered a wrong input!!!")