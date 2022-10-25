# https://docs.python.org/3/library/hashlib.html
import hashlib as _hashlib


class hashlib:
    @staticmethod
    def _cypher(path, cypher):
        with open(path, "rb") as file:
            cypher.update(file.read())
        return cypher.hexdigest().upper()

    @classmethod
    def sha3_512(cls, path):
        return cls._cypher(path, _hashlib.sha3_512())
