from attribute import attribute
from tag import tag


class element:
    def tag(tab, name, body, attribute=''):  # {
        print(tag.start(tab, name, attribute, False))
        body()
        print(tag.end(0, name))

    def _void(tab, name, attribute=[]):
        print(tag.start(tab, name, attribute, True))

    def _text(tab, name, attribute=[]):
        start = tag.start(tab, name, attribute, False)
        end = tag.end(0, name)
        print(start + end)

    def hidden(tab, value, id='', name=''):
        return add.void('input', tab + 0, [
            attribute.id(id),
            attribute.name(name),
            attribute.type('hidden'),
            attribute.value(value)
        ])

    def hiddeno(tab, value, id='', name=''):
        element._void(tab + 0, 'input', [
            attribute.id(id),
            attribute.name(name),
            attribute.type('hidden'),
            attribute.value(value)
        ])

    def canvas(list):
        height = list.pop(0)
        width = list.pop(0)
        element._text(2, 'canvas', [
            attribute.height(height),
            attribute.width(width)
        ])


#element.hiddeno(id='puss', name='piggy', tab=3, value='turky')
#element.canvas(57, 85)
