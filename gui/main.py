import PIL

from window import window

from list import list


icon1 = PIL.Image.open("character.jpg")
icon2 = PIL.Image.open("logo.jpg")
icon3 = PIL.Image.open("victory.jpg")


image_list = list()
image_list.add(icon1)
image_list.add(icon2)
image_list.add(icon3)

app = window(image_list)
app.mainloop()
