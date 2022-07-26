from celestine.keyword.main import language
from celestine.keyword.unicode import LOW_LINE

def load_module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = ["celestine"] + list(paths)
    name = ".".join(iterable)
    item = __import__(name)
    for path in paths:
        item = getattr(item, path)
    return item

minimum = {}
maximum = {}

for lang in language:
    module = load_module("language", lang)
    kitty = vars(module)
    fish = {
        key: value
        for key, value
        in kitty.items()
        if not key.startswith(LOW_LINE)
    }
    for key, value in fish.items():
        long = len(value)
        minimum[key] =  min(minimum.get(key, 256), long)
        maximum[key] =  max(maximum.get(key, 0), long)
    print(fish)

print(minimum)
print(maximum)
