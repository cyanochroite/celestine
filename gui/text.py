from convert import convert


#string = input("you ugly")
string = "-🌋 Volca🏕️ Camping🏜️ Desert"


falcon = []

for character in string:
    falcon.append(convert.get(character, str()))

bird = str().join(falcon)

for character in bird:
    print(ord(character), character)

print(bird)
