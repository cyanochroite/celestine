import celestine.application.language
import celestine.application.language.argument
import celestine.application.language.configure
import celestine.application.language.keyword
import celestine.application.language.report
import celestine.application.language.translate
import celestine.application.language.translator

import keyword

from celestine.core import load

def format_line(item):
    (key, value) = item
    if not key.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(key) or keyword.issoftkeyword(key):
        raise ValueError("This word is a keyword.")
    value = value.replace('"', "'")
    return F'{key} = "{value}"\n'

class file():
    def __init__(self, name, header, iterable):
        self.name = F"{name}.py"
        self.head = F'"""{header}"""\n'
        self.body = map(self.line, iterable)

    def save(self, directory, *paths):
        """Save the items."""
        path = load.path(directory, *paths, self.name)
        with open(path, WRITE, encoding=UTF_8) as file:
            file.write(self.head)
            file.writelines(self.body)
    
    @staticmethod
    def line(item):
        (key, value) = item
        if not key.isidentifier():
            raise ValueError("Not a valid identifier.")
        if keyword.iskeyword(key) or keyword.issoftkeyword(key):
            raise ValueError("This word is a keyword.")
        value = value.replace('"', "'")
        return F'{key} = "{value}"\n'
    


cat = file("cow", "eat some dirt", ["fish=paste", "dogg=hair"])
cat.save("hippo", "pie", "dirt")

print("a".isidentifier())
print("".isidentifier())
print('"'.isidentifier())
print("'".isidentifier())
print("_".isidentifier())
print("3".isidentifier())
format
line