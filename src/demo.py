from pprint import pprint


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)


print(Person.age)

john = Person('John', 18)
pprint(john.__dict__)

john.age = 19
pprint(Person.__dict__)