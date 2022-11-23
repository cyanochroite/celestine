import io


string = io.StringIO()
string.write("I ate a puppy\nYum Yum.\n")
string.write("I sat on a puppy\n")
string.write("I ran over a puppy\n\nWhat fun!\n")

string.seek(0, io.SEEK_SET)

while True:
    line = string.readline()

    if not line:
        break

    print(line)

string.close()
