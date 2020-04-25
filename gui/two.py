from Frame import Frame


class two(Frame):
    def _make(self):
        index = 0
        self.icon = []
        for row in range(3):
            self.icon.append([])
            for column in range(4):
                get = self.data.image_list._list[index]
                but = self.button(width=128, height=128, image=get)
                self.icon[row].append(but)
                index += 1

    def _show(self):
        for row in range(3):
            for column in range(4):
                self.icon[row][column].grid(row=row, column=column)
