def package(name):
    try:
        return __import__(name)
    except ModuleNotFoundError:
        return None
