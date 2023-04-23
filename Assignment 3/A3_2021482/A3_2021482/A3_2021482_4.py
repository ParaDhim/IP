class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def object_info(self):
        print(self.firstname,self.lastname,self.age)

def sort_attribute(query,lst):
    if query == "firstname":
        for i1 in range(0,len(lst) - 1):
            for j1 in range(0,len(lst) - i1 - 1):
                if ord(lst[j1][0][0]) > ord(lst[j1+1][0][0]):
                    lst[j1],lst[j1 + 1] = lst[j1 + 1],lst[j1]

    if query == "lastname":
        for i1 in range(0,len(lst) - 1):
            for j1 in range(0,len(lst) - i1 - 1):
                if ord(lst[j1][1][0]) > ord(lst[j1+1][1][0]):
                    lst[j1],lst[j1 + 1] = lst[j1 + 1],lst[j1]

    if query == "age":
        for i1 in range(0,len(lst) - 1):
            for j1 in range(0,len(lst) - i1 - 1):
                if int(lst[j1][2]) > int(lst[j1+1][2]):
                    lst[j1],lst[j1 + 1] = lst[j1 + 1],lst[j1]
C= "Y"
while C == "Y":
    lst1 = []
    print("Welcome to the Application!")
    n = int(input("Specify number of people to be enrolled: "))
    for i in range(n):
        firstname = input(f"Enter Firstname for Person {i+1}: ")
        lastname = input(f"Enter Lastname for Person {i+1}: ")
        age = int(input(f"Enter Age for Person {i+1}: "))
        lst2 = []
        lst2.append(firstname)
        lst2.append(lastname)
        lst2.append(age)
        lst1.append(lst2)
    que = int(input("Specify number of Queries: "))
    for i2 in range(1,que+1):
        query = input(f"Query{i2}: ")
        if query == "firstname":
            print("Order:")
            sort_attribute(query,lst1)
            for j in range(len(lst1)):
                start_prob = Person(lst1[j][0],lst1[j][1],str(lst1[j][2]))
                start_prob.object_info()
        if query == "lastname":
            print("Order:")
            sort_attribute(query,lst1)
            for j in range(len(lst1)):
                start_prob = Person(lst1[j][0],lst1[j][1],str(lst1[j][2]))
                start_prob.object_info()
        if query == "age":
            print("Order:")
            sort_attribute(query,lst1)
            for j in range(len(lst1)):
                start_prob = Person(lst1[j][0],lst1[j][1],str(lst1[j][2]))
                start_prob.object_info()
        C = ("Thanks for using the Application, if you wish to restart, press “Y” else press “N” to exit: N")
        if C != "Y":
            print("Exits!")
    # for j in range(len(lst1)):

    #     start_prob = Person(lst1[j][0],lst1[j][1],str(lst1[j][2]))
    #     # sort_attribute(query,lst1)
    #     start_prob.object_info()