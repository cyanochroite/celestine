""""""


from celestine.package import Abstract


class Package(Abstract):
    """"""

    def __init__(self, ring, /, name, **star):
        super().__init__(ring, name, pypi="bpy")
