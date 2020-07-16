import pathlib


class Path:
    @classmethod
    def Make(self, path):
        return pathlib.Path(path)

    @classmethod
    def Join(self, one, two):
        return one.joinpath(two)
