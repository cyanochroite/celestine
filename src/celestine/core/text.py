# eventually will do more then just print to terminal
# but setting this up now so can try to use this elsewhere
class log():
    @staticmethod
    def fatal(text):  # user: program will crash now
        print(text)

    @staticmethod   # user: something bad happened
    def error(text):
        print(text)

    @staticmethod
    def warning(text):  # user: things are not perfect right now
        print(text)

    @staticmethod
    def notice(text):  # user: happy text for user to read on terminal
        print(text)

    @staticmethod
    def alert(text):  # dev: dev: exception was thrown
        print(text)

    @staticmethod
    def debug(text):  # dev: temporary printing to see whats wrong
        print(text)

    @staticmethod
    def info(text):  # dev: events that happen
        print(text)

    @staticmethod
    def trace(text):  # dev: crazy logging of everything
        print(text)
