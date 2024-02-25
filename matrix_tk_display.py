import tkinter
from tkinter import Label, Frame, Entry, Button
from common import selected


def please_identify(yourself):
    if type(yourself) == Matrix_Entry:
        print(yourself.position)
        selected["rowA"] = yourself.position[0]
    elif type(yourself) == Matrix_Grid:
        print(yourself.name)
        selected["matrixA"] = yourself.name


def identify(yourself):
    return lambda: please_identify(yourself)


# class Matrix_Entry(Label):
# class Matrix_Entry(Entry):
class Matrix_Entry(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = (0, 0)
        self.entry = None


class Matrix_Entry_Editable(Entry):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = (0, 0)
        self.entry = None


class Matrix_Grid(list):
    ENTRY_WIDTH = 4

    def __init__(self, values, tk_master, name, type):
        super().__init__()
        self.name = name
        self.entries = values
        self.brackets = Button(master=tk_master, text="", borderwidth=1, relief="solid",
                               width=2 + (self.ENTRY_WIDTH + 2) * self.entries.number_of_columns,
                               height=-1 + (self.ENTRY_WIDTH - 2) * self.entries.number_of_rows)
        self.brackets.configure(command=identify(self))
        self.brackets.grid(row=2, column=1, columnspan=3)
        self.container = Frame(master=tk_master)
        self.container.grid(row=1, column=2, rowspan=3)
        for row_number in range(self.entries.number_of_rows):
            self.append([])
            for column_number in range(self.entries.number_of_columns):
                if type == "editable":
                    self[row_number].append(Matrix_Entry_Editable(master=self.container, width=self.ENTRY_WIDTH))
                    # try:
                    self[row_number][column_number].delete(0, tkinter.END)
                    self[row_number][column_number].insert(string=(self.entries[row_number][column_number]), index=0)
                    self[row_number][column_number].configure(font=("Arial", 17, "normal"))
                    # breakpoint()
                else:
                    self[row_number].append(Matrix_Entry(master=self.container, width=self.ENTRY_WIDTH
                                                         , padx=4, pady=4,
                                                         text=self.entries[row_number][column_number]))
                    self[row_number][column_number].position = (row_number, column_number)
                    self[row_number][column_number].configure(command=identify(yourself=self[row_number][column_number]))
                self[row_number][column_number].entry = self.entries[row_number][column_number]
                self[row_number][column_number].grid(row=row_number, column=column_number)

# -------------------------------------#


