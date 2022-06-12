import dearpygui.dearpygui as dpg

file = "D:\\file\\anitest.gif"



def cat(window):
    window.load_image(path)
    
    
    
    
    dpg.create_context()
    
    width, height, channels, data = dpg.load_image(path)
    
    with dpg.window(label="Tutorial"):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")
        dpg.add_image("texture_tag")



def cat(self):
    image = self.image_load("D:\\file\\anitest.gif")
    self.label_add(image)






def main(window):
    window.run(cat)
