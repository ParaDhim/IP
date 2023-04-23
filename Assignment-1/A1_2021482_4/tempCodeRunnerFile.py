    for b2 in range(1,-1,-1):
        for b3 in range(1,-1,-1):
            Fn = (b1 or b2) and (b2 or (not b3))
            if (bool(Fn) == True):
                print("Satisfiable")
                if (count==0):
                    print(bool(b1),bool(b2),bool(b3))#bool(not b3),bool(b1 or b2),bool(b2 or (not b3)),bool(Fn))
                    count += 1