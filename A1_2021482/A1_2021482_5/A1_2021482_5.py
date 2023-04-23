def getReverse(n):
    h=""
    for i in range(1,len(str(n))+1):
        f = ((int(n))%10)
        h = h + str(f)
        n = (int(n))//10
    return h
def checkPalindrome(n):
    a = n
    h = ""
    for i in range(1,len(str(n))+1):
        f = ((int(n))%10)
        h = h + str(f)
        n = (int(n))//10
    if (str(h) == str(a)):
        return True
    else:
        return False
def checkNarcissistic(n):
    a = n
    h = 0
    for i in range(0,len(str(n))):
        f = ((int(n))%10)
        h = int(h) + ((int(f)**3))
        n = (int(n))//10
    if (h == a):
        return True
    else:
        return False
def findDigitSum(n):
    h = 0
    for i in range(0,len(str(n))):
        f = ((int(n))%10)
        h = int(h) + (int(f))
        n = (int(n))//10
    return h
def findSquareDigitSum(n):
    h = 0
    for i in range(0,len(str(n))):
        f = ((int(n))%10)
        h = int(h) + ((int(f)**2))
        n = (int(n))//10
    return h
print("""Hello User, Welcome to the Application. Please select one of the following operations.
1. Find reverse of a number
2. Check whether a number is a palindrome or not.
3. Check whether a number is a Narcissistic number or not.
4. Find the sum of digits of a number
5. Find the sum of squares of digits of a number.
6. Select 6 to exit the application""")
fxn = int(input("Enter the number: "))
if fxn == 1:
    num = int(input("Enter the value: "))
    a = getReverse(num)
    print("The reverse digit is: ",a)
elif fxn == 2:
    num = int(input("Enter the value: "))
    a = checkPalindrome(num)
    print(a)
elif fxn == 3:
    num = int(input("Enter the value: "))
    a = checkNarcissistic(num)
    print(a)
elif fxn == 4:
    num = int(input("Enter the value: "))
    a = findDigitSum(num)
    print("The sum of the digit is :",a)
elif fxn == 5:
    num = int(input("Enter the value: "))
    a = findSquareDigitSum(num)
    print("The sum of the square of the digits of the no. is: ",a)
else:
    print("Exited")
