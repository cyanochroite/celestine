class tag:
    def _prefix(tab):
        return '{}<'.format('\t' * tab)

    def _infix(left, right):
        return '{}{}'.format(left, right)

    def _postfix(void):
        return '{}>'.format(' /' if void else '')

    def start(tab, name, attribute=[], void=False):  # {
        prefix = tag._prefix(tab)
        infix = tag._infix(name, ''.join(attribute))
        postfix = tag._postfix(void)
        return '{}{}{}'.format(prefix, infix, postfix)

    def end(tab, name):
        prefix = tag._prefix(tab)
        infix = tag._infix('/', name)
        postfix = tag._postfix(False)
        return '{}{}{}'.format(prefix, infix, postfix)
