
from celestine.session.argument import Argument
from celestine.session.configuration import Configuration
from celestine.session.python import python

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK


class Parser():
    def __init__(self, directory):
        self.directory = directory

        self.argument = Argument()
        config = Configuration(directory)
        self.configuration = config.load(directory)
        self.default = config.load_default(directory)

    
    def load_application(self):
        try:
            argumentation = sys.argv[1]
            if argumentation not in applications:
                parser.parse_args()
        except IndexError:
            try:
                configuration = configuration.load(directory, CELESTINE, CONFIGURATION)
                argumentation = configuration[CELESTINE][APPLICATION]
            except KeyError:
                configuration = configuration.load_default()
                argumentation = configuration[CELESTINE][APPLICATION]
        return load.module(APPLICATION, argumentation)


    def load_attribute(self, attribute):
        cat = getattr(argument, attribute)
        if cat:
            return cat
                
        try:
            argg = self.configuration[CELESTINE][APPLICATION]
        except KeyError:
            argg = self.default[CELESTINE][APPLICATION]
        return argg

    def parse(self, session):
        argument = session.argument.parser.parse_args()
        application = self.load_attribute(argument, APPLICATION)
        task = self.load_attribute(argument, TASK)
        language =self.load_attribute(argument, LANGUAGE)

        self.load_attribute()
        session.application = module(APPLICATION, application)
        session.task = module(APPLICATION, application, argument)
        session.language = module(LANGUAGE, language)
        session.asset = sys.path[0]
