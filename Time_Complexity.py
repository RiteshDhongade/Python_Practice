import time
def timer_test(func):
    def time_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return time_test_inner
@timer_test
def test2():
    print(466+155)

test2()