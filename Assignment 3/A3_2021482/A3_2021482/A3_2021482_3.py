from datetime import datetime

class BankAccount:
    def __init__(self, Name, Password, Start_Balance):
        self.Name = Name
        self.Password = Password
        self.Start_Balance = Start_Balance

        self.f = open(f"{self.Name}.txt","a")
        self.f.close()
    def authenticate(self, pswd):
        if self.Password == pswd:
            return True
        else:
            return False

    def deposit(self,depot):
        b = 0
        for i in range(1,4):
            assert b < 3
            
            try:
                pswd = input("Enter Your Secret Password: ")
                if self.authenticate(pswd) == True:
                    self.Start_Balance += depot
                    self.f = open(f"{self.Name}.txt","a",encoding="utf-8")
                    c = datetime.now()
                    self.f.write(f"{c}The amount of Rupees {depot} has been added   Current Start_Balance → {self.Start_Balance}\n")
                    self.f.close()
                    break
                else:
                    b += 1
                

            except AssertionError:
                print("Too many wrong attempts!!")
                break
            b += 1
    def withdraw(self,withd):
        b = 0
        for i in range(1,4):
            assert b < 3
            
            try:
                pswd = input("Enter Your Secret Password: ")
                if self.authenticate(pswd) == True:
                    self.Start_Balance = self.Start_Balance - withd
                    self.f = open(f"{self.Name}.txt","a",encoding="utf-8")
                    d = datetime.now()
                    self.f.write(f"{d}The amount of Rupees {withd} has been debited   Current Start_Balance → {self.Start_Balance}\n")
                    self.f.close()
                    break
                else:
                    b += 1
                

            except AssertionError:
                print("Too many wrong attempts!!")
            b += 1
    def bankStatement(self):
        b = 0
        for i in range(1,4):
            assert b < 3
            
            try:
                pswd = input("Enter Your Secret Password: ")
                if self.authenticate(pswd) == True:
                    self.f = open(f"{self.Name}.txt","r")
                    for i1 in self.f:
                        print(i1)
                    self.f.close()
                    # self.f.write(datetime.now(),f"The amount of Rupees {depot} has been added Current Start_Balance → {self.Start_Balance}")
                    break
                else:
                    b += 1
                

            except AssertionError:
                print("Too many wrong attempts!!")
            b += 1
print("Welcome to the Bank of IIIT-D")
Name = input("Enter Name: ")
Password = input("Enter Password: ")
Start_Balance = int(input("Starting Start_Balance for your Account: "))

start_prob = BankAccount (Name, Password, Start_Balance)

print("""Select Your Option:
1. Deposit
2. Withdraw
3. Bank Statement""")


C = "Y"
while C == "Y":
    choice = int(input("Enter the value: "))
    if choice == 1:
        depot = int(input("Provide the amount to be deposited: "))
        start_prob.deposit(depot)
    if choice == 2:
        withd = int(input("Provide the amount to be withdrawn: "))
        start_prob.withdraw(withd)
    if choice == 3:
        start_prob.bankStatement()
    C = input("Do you wish to continue? Y/N : ")