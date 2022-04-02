import hashlib
import os
import png
from os import listdir
from os.path import isfile, join

def file_cypher(name):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    cypher = hashlib.sha3_512()
    with open(file_name_data(name), "rb") as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            cypher.update(data)
    return format(cypher.hexdigest())

def file_name_data(name):
    return "data/" + str(name) + ".png"

def file_name_done(name):
    return "done/sha3_512-" + file_cypher(name).upper() + ".png"

def file_name_todo(name):
    return "todo/" + str(name)


def image_write(width,height,compression,name,pixels):
    writer = png.Writer(
        width=width,
        height=height,
        greyscale=False,
        alpha=False,
        bitdepth=8,
        compression=compression,
        interlace=False,
        planes=1
        ).write_array(
            open(name, "wb"),
            pixels
            )

def index_of_smallest_item(array):
    return min(range(len(array)), key=array.__getitem__)

def image_read(name):
    (width, height, pixels, metadata) = png.Reader(file_name_todo(name)).read_flat()
    return (width, height, pixels)

def image_compression(width, height, pixels):
    for compression in range(0,10):
        image_write(width,height,compression,file_name_data(compression),pixels)

def image_compression_winner():
    array = [];
    for compression in range(0,10):
        array.append(os.path.getsize(file_name_data(compression)))
    return index_of_smallest_item(array)

def work_item(name):
    (width, height, pixels) = image_read(name)
    image_compression(width, height, pixels)
    compression = image_compression_winner()
    file_name = file_name_done(image_compression_winner())
    image_write(width,
                height,
                compression,
                file_name,
                pixels)
    print(str(name) + " " + str(compression) + " " + str(file_name))

def file_list(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def work():
    for file in file_list("todo/"):
        work_item(file)
    print("finished")

work()
