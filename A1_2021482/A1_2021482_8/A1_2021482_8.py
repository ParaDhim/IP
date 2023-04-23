c = float(input("Enter the initial cost of car: "))
r = float(input("Enter teh depretiation rate: "))
count = 1
valueDerived = 0
a = 50
for i in range (1,16):
    if (count == 1):
        depreciation = (c*(r/100))
        ut = (6000)*a
        maintain = (c*(1/100))
        valueDerived = valueDerived + maintain + ut
        count += 1
        if valueDerived>c:
            print(i)
            break
        
    elif (1<count<6):
        depreciation = (c*(r/100))
        c = c - depreciation
        a = a*(50/100)
        ut = (6000)*a
        maintain = (c*(1/100))
        valueDerived = valueDerived + maintain + ut
        count += 1
        if valueDerived>c:
            print(i)
            break
    elif (count <= 15) and (count >= 6):
        depreciation = (c*(r/100))
        c = c - depreciation
        a = a*(50/100)
        ut = (6000)*a
        maintain = (c*(50/100))
        valueDerived = valueDerived + maintain + ut
        count += 1
        if valueDerived>c:
            print(i)
            break
    else:
        print("It has been 15 years you may sold it now")