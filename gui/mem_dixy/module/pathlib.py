import pathlib


class Path:
    @classmethod
    def Make(cls, path):
        return pathlib.Path(path)

    @classmethod
    def Join(cls, one, two):
        return one.joinpath(two)
