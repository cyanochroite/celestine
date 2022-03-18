from mem_dixy.package.python.path import path


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
