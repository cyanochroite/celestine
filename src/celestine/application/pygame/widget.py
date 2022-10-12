class Widget():
    def __init__(self, window, item, rectangle):
        position = (rectangle.cord_x, rectangle.cord_y)
        window.blit(item, position)
