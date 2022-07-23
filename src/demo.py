

from celestine.keyword import language
from celestine.keyword.unicode import LOW_LINE
doggy = language
kitty = vars(language)


def check(name):
    return not name.startswith("_")


puppy = filter(check, kitty)
print(list(puppy))

for name, value in kitty.items():
    if not name.startswith("_"):
        print(value)
    if name[0] != "_":
        print(value)
#    print(F"KEY={name} : VALKE={value}")


fish = {
    key: value
    for key, value
    in kitty.items()
    if not key.startswith(LOW_LINE)
}
print(LOW_LINE)

print(fish)
