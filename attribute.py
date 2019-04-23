class attribute:
    def _attribute(name, value):
        return ' {}="{}"'.format(name, value) if (name and value) else ''

    def _boolean(name, test):
        return ' {}="{}"'.format(name, name) if (name and test) else ''

    def autofocus(value):
        return _boolean('autofocus', value)

    def checked(value):
        return _boolean('checked', value)

    def C_ASS():  # class. this one hard
        return ''

    def disabled(value):
        return _boolean('disabled', value)

    def height(value):
        return attribute._attribute('height', value)

    def href():  # this one hard
        return ''

    def id(value):
        return attribute._attribute('id', value)

    def label(value):
        return attribute._attribute('label', value)

    def max(value):
        return attribute._attribute('max', value)

    def min(value):
        return attribute._attribute('min', value)

    def name(value):
        return attribute._attribute('name', value)

    def placeholder(value):
        return attribute._attribute('placeholder', value)

    def readonly(value):
        return _boolean('readonly', value)

    def required(value):
        return _boolean('required', value)

    def selected(selected, value):
        return _boolean('selected', selected and selected == value)

    def style(value):
        return attribute._attribute('style', value)

    def type(value):
        return attribute._attribute('type', value)

    def value(value):
        return attribute._attribute('value', value)

    def width(value):
        return attribute._attribute('width', value)
