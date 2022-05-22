from celestine.parser.translator import translator
from celestine.parser.translator import converter

go = translator()
more = go.translate("ⶀ0#hi35<mo5cat  $&dog")
print(more)
cat = converter.translate(more)
print(cat)

print("moo")