"""Central place for loading and importing external files."""
import keyword

from celestine.core import load

from celestine.keyword.main import WRITE
from celestine.keyword.main import UTF_8


class File():
    """Write a key value pair python file."""
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
        """Make a line for the file from a key value pair."""
        (key, value) = item
        if not key.isidentifier():
            raise ValueError("Not a valid identifier.")
        if keyword.iskeyword(key) or keyword.issoftkeyword(key):
            raise ValueError("This word is a keyword.")
        value = value.replace('"', "'")
        return F'{key} = "{value}"\n'
