import sys
import shutil


def copy(one, two):
    shutil.copytree(src, dst)

def main(argument):
    print(argument)
    src = argument[0]
    dst = argument[1]
    try:
        shutil.copytree(src, dst)
    except:
        print("@")
    finally:
        print("#")
    print("%")

if __name__ == "__main__":
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    sys.exit(main(sys.argv[1:]))

