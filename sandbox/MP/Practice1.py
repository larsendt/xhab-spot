__author__ = 'skynet'

def factorial(n):
    print("Factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res =  n * factorial(n-1)
        print("res is " + str(res))
        return res

def adder(a, b):
    for i in range(1,3):
        print("i is "+str(i))
    while j<10:
        print("j is " + str(j))
        j+=1
    return a + b


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    try:
        raise MyError(2*2)
    except MyError as e:
        print 'My exception occurred, value:', e.value

factorial(4)
print("Adder sum is " + str(adder(2, 4)))