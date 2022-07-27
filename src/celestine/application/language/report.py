from celestine.core import load

from celestine.keyword.main import language
from celestine.keyword.main import LANGUAGE
from celestine.keyword.unicode import LOW_LINE


def main():
    minimum = {}
    maximum = {}
    
    for lang in language:
        module = load.module(LANGUAGE, lang)
        dictionary = load.dictionary(module)
        for key, value in dictionary.items():
            long = len(value)
            minimum[key] =  min(minimum.get(key, 256), long)
            maximum[key] =  max(maximum.get(key, 0), long)
    
    print(minimum)
    print(maximum)
    
