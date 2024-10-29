from function import logit

class A():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @logit #funciona, mas precisaria de mais uma polida para funcionar par classes
    def whoami(self):
        return self.__class__.__name__

a = A(1,2)
print(a.whoami())
print(a.b)