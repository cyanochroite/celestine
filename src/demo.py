"""lazy"""
import configparser
cow = ''
if cow:
    print("hi")
else:
    print("dog")

print('' or 'bacon')

class Attribute():
    def add(self, application, *iterable):
        self.section = application
        for attribute in iterable:
            args = None
            try:
                cat = getattr(self.session.argument, attribute)
                if cat:
                    args = cat
            except AttributeError:
                pass

            if not args:
                try:
                    args = self.session.configuration[self.section][attribute]
                except KeyError:
                    args = self.session.default[self.section][attribute]

            setattr(self, attribute, args)  # value

        return self



class Application():
    """pointless"""
    
    def __getattr__(self, key):
        if key == 'Foo':
            return cls._foo_func()
        elif key == 'Bar':
            return cls._bar_func()
        raise AttributeError(key)    
    
    def __init__(self):
        self.configuration = configparser.ConfigParser()


    def add_configuration(self, application):
        self.configuration.add_section(application)

        attribute = self.attribute()
        default = self.default()
        for item in zip(attribute, default, strict=True):
            (name, value) = item
            self.configuration.set(application, name, value)

    def configtree(self):
        self.add_configuration("celestine")
        self.add_configuration("tkinter")
    
    def argument(self, argument):
        """Build up the argument."""
        return argument

    def attribute(self):
        """Build up the attribute file."""
        print("moo")
        return ()

    def default(self):
        """Build up the argument."""
        print("hi")
        return ()


class Cow(Application):
    """needed"""

    def argument(self, argument):
        print("woof")
        return argument

    def attribute(self):
        print("meaw")
        return ()

    def default(self):
        print("bye")
        return ()


hat = Cow()

hat.configtree()
hat.doggy
