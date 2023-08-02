class class1 :
    def test_class1(self) :
        print("this is class1")
class class2(class1) :
    def test_class2(self) :
        print("this is class2")
class class3(class2) :
    def test_class3(self) :
        print("this is class3")
obj_class3 = class3()
obj_class3.test_class1()
                        