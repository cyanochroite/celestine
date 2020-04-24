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


#a = Foo()
#b = Bar()
c = Baz().suck()
