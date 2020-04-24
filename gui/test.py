import abc


class Foo(metaclass=abc.ABCMeta):
    def suck(self):
        self.foo()

    @abc.abstractmethod
    def foo(self):
        print("yo mom")
        pass


class Bar(Foo):
    pass


class Baz(Bar):
    def foo(self):
        print("a cow")
        return super(Baz, self).foo()


class demo():
    def __init__(self, **key):
        # print(key["stone"])
        print(key["moo"])
        print(key)


#a = Foo()
#b = Bar()
c = Baz().suck()
n = demo(moo="hy", coo="mo")
