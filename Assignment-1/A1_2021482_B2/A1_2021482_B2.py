import math
e = [float(i) for i in input().split()]#orign
d = [float(j) for j in input().split()]#direction
center = [float(k) for k in input().split()]
R = int(input("Enter the value for R: "))
x0 = e[0]
y0 = e[1]
z0 = e[2]
# if (((x1 - x0)**2) + ((y1 - y0)**2) + ((z1 - z0)**2) - (R**2)) == 0:
# if (((x1 - x0)**2) + ((y1 - y0)**2) + ((z1 - z0)**2) - (R**2)) < 0:
# if (((x1 - x0)**2) + ((y1 - y0)**2) + ((z1 - z0)**2) - (R**2)) > 0:
a = d[0]*d[0] + d[1]*d[1] + d[2]*d[2]
b = 2*d[0]*(x0-center[0]) + 2*d[1]*(y0-center[1]) + 2*d[2]*(z0-center[2])
c = center[0]*center[0] + center[1]*center[1] + center[2]*center[2] + x0*x0 + y0*y0 + z0*z0 + -2*(center[0]*x0 + center[1]*y0 + center[2]*z0) - R*R
D = b**2 - 4*a*c
if D < 0:
    print("NO INTERSECTION")
elif D == 0:
    print("INTERSECT AT ONLY ONE POINT OR THE RAY IS TANGENT TO THE SPHERE")
    t = ((-b + ((D)**0.5))/(2*a))
    print(int(t))
elif D > 0:
    print("THE RAY INTERSECT TO THE SPHERE AT TWO DISTINCT POINT")
    t1 = ((-b + ((D)**0.5))/(2*a))
    t2 = ((-b - ((D)**0.5))/(2*a))
    print("The first Point is",math.ceil(t1),",The second point is",math.ceil(t2))
