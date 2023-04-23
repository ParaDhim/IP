count = 0
"""If we need to do it for a single function we can do it by uncommenting the 1 sustitute and 2 substitute
and commenting the other 2 function after which in comment 1 and 2 """

for b1 in range(1,-1,-1):
    Fn = ((b1) and (not b1))#1-----
    #Fn = (b1 or b2) and (b2 or (not b3)) #1 substitue
    if (bool(Fn) == True):
        print(bool(b1),bool(not b1),print(Fn))
    elif (bool(Fn) == False):
        print("Unsatisfiable")
for b1 in range(1,-1,-1):
    for b2 in range(1,-1,-1):
        for b3 in range(1,-1,-1):
            Fn = (b1 or b2) and (b2 or (not b3))#2------
            # Fn = (b1 or b2) and (b2 or (not b3)) #2 substitue
            if (bool(Fn) == True):
                """coment from here if just need one case and print of it"""
                print("Satisfiable")
                if (count==0):
                    print(bool(b1),bool(b2),bool(b3))
                    count += 1
                """till here"""
                 #and uncomment the below 4 lines
                """if (count==0):
                    print("Satisfiable")
                    print(bool(b1),bool(b2),bool(b3))
                    count += 1
                    break"""
                
            