class A():
    def food(self):
        super().food()
        print('A.food()')


class B():
    def food(self):
        print('B.food()')


class C(A, B):
    def food(self):
        super().food()
        print('C.food()')


cat = C()
cat.food()


class AAA:
    def __init__(self):
        self.hat = 0

    def cat(self):
        print("HI")


class BBB:
    def __init__(self):
        self.item = {}

    def cat(self):
        print("moo")


class Page(BBB, AAA):
    def __init__(self, window, document):
        super().__init__()

    def cat(self):
        super().cat()
        print("oink")


pat = Page(None, None)
pat.cat()
