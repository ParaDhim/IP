
class Company:
    def __init__(self, Comp_Name, Requiredcgpa, branches, positionOpen):
        self.Comp_Name = Comp_Name
        self.Requiredcgpa = Requiredcgpa
        self.branches = branches
        self.positionOpen = positionOpen
        self.appliedStudents = []
        self.applicationOpen = True

    def hireStudents(self):
        # count=0
        for i in self.appliedStudents:
            if(self.positionOpen>0):
                # print(i.Name)
                i.getsPlaced()
                self.positionOpen-=1
                # count+=1
        # print("Company hired ",count,"students")
        self.closeApplication()

    def closeApplication(self):
        print(f"The {self.Comp_Name} has hired the following Students : ")
        count=0
        for i in self.appliedStudents:
            if(i.lst_Placed==True):
                print(i.Name)
                count+=1
        print("Company has hired ",count,"Students")
        self.applicationOpen=False






class Student:
    def __init__(self, Name, cgpa, branch):
        self.Name = Name
        self.cgpa = cgpa
        self.branch = branch
        self.lst_Placed = False

    def isEligible(self, C_name):
        if self.cgpa >= C_name.Requiredcgpa and self.branch in C_name.branches and self.lst_Placed==False:
            print("Student ",self.Name," is Eligible for the Company ",C_name.Comp_Name) 
            self.apply(C_name)          
        else:
            print("Student ",self.Name," is not Eligible for the Company ",C_name.Comp_Name)            



    def apply(self, C_name):
        C_name.appliedStudents.append(self)
    def getsPlaced(self):
        self.lst_Placed=True

    # def listElements(self):
    #     l1 = [i1 for i1 in self.name]
    #     l1 = [i2 for i2 in self.name]
    #     l1 = [i3 for i3 in self.name]
    #     l1 = [i4 for i4 in self.name]
    #     l1 = [i5 for i5 in self.name]


lst1 = []
n = int(input("Enter the number of students: \n"))
for i in range(n):
    Name = input(f"Enter the name of student {i + 1}: ")
    cgpa = float(input(f"Enter the cgpa of {i + 1}: "))
    branch = input(f"Enter the branch of student {i + 1}: ")
    s=Student(Name,cgpa,branch)
    lst1.append(s)



lst3 = []
n = int(input("Enter the number of Companies: \n"))
for i3 in range(n):
    Comp_Name = input(f"Enter the name of Comapany {i3 + 1}: \n")
    Requiredcgpa = float(input(f"Enter the required cgpa of Company {i3 + 1}: "))
    branches = [br for br in input(f"Enter the branches accepted by Company {i3 + 1} (space seperated): ").split(" ") ]
    positionOpen = int(input(f"Enter the number of positions Open of Comapany {i3 + 1}: \n"))
    C=Company(Comp_Name,Requiredcgpa,branches,positionOpen)
    # lst3.append(C)
    for i in lst1:
        i.isEligible(C)
    C.hireStudents()
    