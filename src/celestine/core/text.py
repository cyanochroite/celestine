fatal = True
error = True
notice = True
warning = True
alert = True
debug = True
info = True
trace = True

# eventually will do more then just print to terminal
# but setting this up now so can try to use this elsewhere
class log():
    @staticmethod
    def fatal(text):  # user: program will crash now
        if fatal:
            print(text)

    @staticmethod
    def error(text):  # user: something bad happened
        if error:
            print(text)

    @staticmethod
    def notice(text):  # user: happy text for user to read on terminal
        if notice:
            print(text)

    @staticmethod
    def warning(text):  # user: things are not perfect right now
        if warning:
            print(text)

    @staticmethod
    def alert(text):  # dev: dev: exception was thrown
        if alert:
            print(text)

    @staticmethod
    def debug(text):  # dev: temporary printing to see whats wrong
        if debug:
            print(text)

    @staticmethod
    def info(text):  # dev: events that happen
        if info:
            print(text)

    @staticmethod
    def trace(text):  # dev: crazy logging of everything
        if trace:
            print(text)


"""

<a href="#" class="link-primary">Primary link</a>
<a href="#" class="link-secondary">Secondary link</a>
<a href="#" class="link-success">Success link</a>
<a href="#" class="link-danger">Danger link</a>
<a href="#" class="link-warning">Warning link</a>
<a href="#" class="link-info">Info link</a>
<a href="#" class="link-light">Light link</a>
<a href="#" class="link-dark">Dark link</a>

Warning
Error
Info
Debug
Exception

TRACE DEBUG INFO WARN ERROR OFF

#user
FATAL
ERROR
WARNING
NOTICE

#developer
ALERT
DEBUG
INFO
TRACE

Debug
notice 

FATAL
ERROR
WARNING
INFO
DEBUG
TRACE


10

NOTSET


ALL 	All levels including custom levels.
DEBUG 	Designates fine-grained informational events that are most useful to debug an application.
INFO 	Designates informational messages that highlight the progress of the application at coarse-grained level.
WARN 	Designates potentially harmful situations.
ERROR 	Designates error events that might still allow the application to continue running.
FATAL 	Designates very severe error events that will presumably lead the application to abort.
OFF 	The highest possible rank and is intended to turn off logging.
TRACE 	Designates finer-grained informational events than the DEBUG.
"""
