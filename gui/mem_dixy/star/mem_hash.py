import hashlib


class mem_hash:
    def file_cypher(path):
        cypher = hashlib.sha3_512()
        with open(path, "rb") as file:
            cypher.update(file.read())
        return cypher.hexdigest().upper()
