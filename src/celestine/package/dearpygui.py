from celestine.package.python.path import path


# I forgot what I used this for:
class file_dialog():
    @staticmethod
    def selection(app_data):
        array = []
        current_path = app_data["current_path"]
        directory = path.dirname(current_path)
        selections = app_data["selections"]
        for selection in selections:
            file = path.basename(selection)
            item = path.join(directory, file)
            array.append(item)
        return array



return internal_dpg.load_image(file, gamma=gamma, gamma_scale_factor=gamma_scale_factor, **kwargs)


def load_image(file: str, gamma: float = 1.0, gamma_scale_factor: float = 1.0):
    (width, height, channels, data) = dpg.load_image(
        file,
        gamma=gamma,
        gamma_scale_factor=gamma_scale_factor
    )
    
    print(width)
    pass


load_image("cat")