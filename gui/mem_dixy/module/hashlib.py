import hashlib


class Hash:
    @classmethod
    def _cypher(cls, path, cypher):
        with open(path, "rb") as file:
            cypher.update(file.read())
        return cypher.hexdigest().upper()

    @classmethod
    def sha3_512(cls, path):
        return cls._cypher(path, hashlib.sha3_512())
