import celestine.python.python_3_7
import celestine.python.python_3_8
import celestine.python.python_3_9

def parse_package(package):
    match parse_package(parse.package):
        case "unittest":
            sys.argv = [sys.argv[0]]  # clear argument list
            # Import everything so we can find tests.
            # This can only be done from the top level, so that is why it is here.
            from celestine.package.unittest import *
            # Also we only attempt to import unittest if the user requested it.
            # This is because it could not be installed and would error otherwise.
            import unittest
            unittest.main()  # this function will terminate the program
        case "celestine":
            pass
        case _ as package:
            module = load.package(package)
            window = module.Window()
            run = main(session)
            window.run(run)