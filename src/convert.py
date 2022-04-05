import PIL.Image;
import os;
import hashlib;

def image_open(path):#{
    return PIL.Image.open(path);
#}

def image_new(size):#{
    mode = "RGBA";
#    size = size;
    color = (0x00,0x00,0x00,0x00);
    return PIL.Image.new(mode,size,color);
#}

def image_save(image, path):#{
    if os.path.isfile(path):#{
        os.remove(path);
    #}
    with open(path, "wb") as file:#{
        image.save(file, "PNG", optimize=True);
    #}
#}
        
def file_cypher(path):#{
    cypher = hashlib.sha3_512();
    with open(path, "rb") as file:#{
        cypher.update(file.read());
    #}
    return cypher.hexdigest().upper();
#}
    
def os_rename(open_spot, save_path):#{
    save_spot = save_path + file_cypher(open_spot) + ".png";
    if not os.path.isfile(save_spot):#{
        os.rename(open_spot, save_spot);
    #}
#}

def file_save(load_file):#{
    load_path = "D:/todo/"
    save_path = "D:/done/";
    save_file = "demo.png";
    base = image_open(load_path + load_file);
    image = image_new(base.size);
    image.paste(base);
    image_save(image, save_path + save_file);
    os_rename(save_path + save_file, save_path);
#}
print("scan");


file_save("Control_Screenshot_2.jpg");
file_save("Control_Screenshot_3.jpg");


print("done");
