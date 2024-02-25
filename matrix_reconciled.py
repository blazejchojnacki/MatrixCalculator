import matrix_math
import matrix_history
import matrix_tk_display


class Matrix_Selectable:
    def __init__(self, name, entries, tk_master):
        self.tk_master = tk_master
        self.name = name
        self.entries = matrix_math.Matrix(entries)
        self.display = matrix_tk_display.Matrix_Grid(self.entries, tk_master=tk_master, name=name, type="selectable")
        self.history = matrix_history.Recaller(self.entries, name)

    def convert(self, editable_matrix):
        # if len(self.display) != len(self.entries):
        try:
            self.entries = editable_matrix.entries
            self.entries.number_of_rows = len(self.entries)
            self.entries.number_of_columns = len(self.entries[0])
            # breakpoint()
            self.display = matrix_tk_display.Matrix_Grid(editable_matrix.entries, tk_master=self.tk_master,
                                                         name=self.name, type="selectable")
        except TypeError:
            print("wrong type")


class Matrix_Editable:
    def __init__(self, name, entries, tk_master):
        self.entries = matrix_math.Matrix(entries)
        self.display = matrix_tk_display.Matrix_Grid(self.entries, tk_master=tk_master, name=name, type="editable")
        self.history = matrix_history.Recaller(self.entries, name)

