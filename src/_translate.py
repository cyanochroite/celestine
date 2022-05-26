from celestine.parser.translator import translator
from celestine.parser.translator import tokenizer
from celestine.parser.translator import parser

one = translator.translate("ⶀ<>0#h i35 <m o7cat  $&dog")
print(list(one))
two = tokenizer.tokenize(one)
print(list(two))
three = parser.parse(two)
print(list(three))
print("moo")



from celestine.parser.operator import *
print(Unary.STAR.value)