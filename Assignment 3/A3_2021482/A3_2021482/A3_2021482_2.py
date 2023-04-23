from xmlrpc.client import Boolean


class LaundryService:
    def __init__(self, NameOfCustomer, ContactOfCustomer, Email, TypeOfCloth, Branded, Season):
        id_Customer = 0
        self.NameOfCustomer = NameOfCustomer
        self.ContactOfCustomer = ContactOfCustomer
        self.Email = Email
        self.TypeOfCloth = TypeOfCloth
        self.Branded = Branded
        self.total_charge = 0
        self.Season = Season
        # global id_Customer
        # id_Customer += 1
        # self.id_Customer = id_Customer
    def customerDetails(self):
        # print("The customer specific details:\n")
        # print("Customer Id :",self.id_Customer)
        print("Customer Name :",self.NameOfCustomer)
        print("Contact :",self.ContactOfCustomer)
        print("Email :",self.Email)
        print("Type of cloth :",self.TypeOfCloth)
        print("Branded or not :",self.Branded)

    def calculateCharge(self):
        if self.TypeOfCloth == "Cotton":
            self.total_charge = self.total_charge + 50
        elif self.TypeOfCloth == "Silk":
            self.total_charge = self.total_charge + 30
        elif self.TypeOfCloth == "Woolen":
            self.total_charge = self.total_charge + 90
        elif self.TypeOfCloth == "Polyester":
            self.total_charge = self.total_charge + 20

        if self.Branded == True:
            self.total_charge = self.total_charge * 1.5
        elif self.Branded == False:
            self.total_charge = self.total_charge
        if self.Season == "Winter":
            self.total_charge = self.total_charge * 0.5
        else:
            self.total_charge = self.total_charge * 2
        return self.total_charge
    def finalDetails(self):
        if self.total_charge > 200:
            # a = self.total_charge
            print("Total charge: ",(self.total_charge))
            print("To be returned in 4 days")
        else:
            print("Total charge: ",(self.total_charge))
            print("To be returned in 7 days")
    
num = int(input("Enter the value for which you would like to repeat: "))
customer_Id = 0

for ij in range(0,num):
    customer_Id += 1
    NameOfCustomer = input("Name of customer: ")
    ContactOfCustomer = input("Contact No.: ")
    Email = input("Email: ")
    TypeOfCloth = input("Type of Cloth: ")
    Branded = bool(int(input("Branded?: ")))
    Season = input("Season: ")
    Custmer_Cal = LaundryService(NameOfCustomer, ContactOfCustomer, Email, TypeOfCloth, Branded, Season)
    print("The customer specific details:\n")
    print("Customer Id: ",customer_Id)
    Custmer_Cal.customerDetails()
    Custmer_Cal.calculateCharge()
    Custmer_Cal.finalDetails()
    