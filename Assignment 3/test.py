class test:
    def __init__(self,name):
        self.name=name
        # self.name=test.name
    def nch(self,nope):
    # def name(self):
    #     return self.name
        self.name = nope
        return test.name

k = test("kuch")        
# def test1():
#     print(test.name())
print(test.name)
print(k.nch("poppey"))
# print(test.name)