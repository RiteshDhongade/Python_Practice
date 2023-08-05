def deco(func):
    def inner_deco():
        print("This is start of function")
        func()
        print("This is end of function")
    return inner_deco
@deco
def test1():
    print(4+5)

test1()