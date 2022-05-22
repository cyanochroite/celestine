from celestine.parser.translator import translator
from celestine.parser.translator import converter

go = translator()
more = go.translate("hi35<mo5cat$&dog")
cat = converter.translate(more)
print(cat)

print("moo")