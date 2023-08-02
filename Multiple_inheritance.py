class class1:
    def test_class1(self):
        print("this is class 1")
class class2:
    def test_class1(self):
        print("this is class 2")  
class class3 (class1 , class2):
    pass
obj_class3 = class3()
obj_class3.test_class1()
              