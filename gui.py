from tkinter import Button, Label, Frame
import matrix_operations


class Matrix_Entry(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = (0, 0)
        self.entry = None


class Matrix_Grid(list):
    ENTRY_WIDTH = 4
    # the following creates a new window to display things
    # brackets = {
    #     "left up": Label(text="⸢", width=1, font=("calibri", 20, "normal")),
    #     "left center": [],
    #     "left down": Label(text="⸤", width=1, font=("calibri", 20, "normal")),
    #     "right up": Label(text="⸣", width=1, font=("calibri", 20, "normal")),
    #     "right center": [],
    #     "right down": Label(text="⸥", width=1, font=("calibri", 20, "normal")),
    # }

    def __init__(self, entries):
        super().__init__()
        self.entries = entries
        self.rect = Label(text="", width=(self.ENTRY_WIDTH + 3) * (self.entries.number_of_columns + 0), height=6, borderwidth=2, relief="solid")
        self.container = Label()
        for row_number in range(self.entries.number_of_rows):
            self.append([])
            # self.brackets["left center"].append(Label(text="|", width=1, font=("calibri", 14, "normal")))
            # self.brackets["right center"].append(Label(text="|", width=1, font=("calibri", 15, "normal")))
            for column_number in range(self.entries.number_of_columns):
                self[row_number].append(Matrix_Entry(master=self.container, width=self.ENTRY_WIDTH))
                self[row_number][column_number].position = (row_number, column_number)
                self[row_number][column_number].entry = self.entries[row_number][column_number]
                self[row_number][column_number].config(padx=5, pady=5, text=self.entries[row_number][column_number])

    def place(self, begin_row, begin_column):
        # self.brackets["left up"].grid(row=begin_row, column=begin_column, rowspan=2)
        # self.brackets["left down"].grid(row=begin_row + self.entries.number_of_rows, column=begin_column, rowspan=2)
        #
        # self.brackets["right up"].grid(row=begin_row,
        #                                column=begin_column + self.entries.number_of_columns + 1, rowspan=2)
        # self.brackets["right down"].grid(row=begin_row + self.entries.number_of_rows,
        #                                  column=begin_column + self.entries.number_of_columns + 1, rowspan=2)
        self.rect.grid(row=begin_row + 1, column=begin_column, columnspan=3)
        self.container.grid(row=begin_row, column=begin_column + 1, rowspan=3)
        for row_number in range(self.entries.number_of_rows):
            # self.brackets["left center"][row_number].grid(row=begin_row + row_number, column=begin_column, rowspan=2)
            # self.brackets["right center"][row_number].grid(row=begin_row + row_number, rowspan=2,
            #                                                column=begin_column + self.entries.number_of_columns + 1)
            for column_number in range(self.entries.number_of_columns):
                self[row_number][column_number].grid(row=row_number, column=column_number)

# -------------------------------------#


def command_interpreter(command, matrix_a=None, matrix_b=None):
    operands = {
        "matrix_A": [[]],
        "matrix_B": [[]],
        "row_a": None,
        "row_b": None,
        "scalar": 1,
        "function": None,
    }
    if matrix_a is not None:
        operands["matrix_A"] = matrix_a
    if matrix_b is not None:
        operands["matrix_B"] = matrix_b

    # operation_dict = {
    #     "transpose": matrix_operations.transpose,
    #     "invert": matrix_operations.inverse,
    #     "det": matrix_operations.get_determinant,
    #     "+": matrix_operations.add,
    #     "-": matrix_operations.subtract,
    # }
    for key in matrix_operations.operation_dict:
        if key in command:
            operands["function"] = matrix_operations.operation_dict[key]
            command = command.replace(key, "")

    for i in range(1, 10):
        if f"R{i}" in command:
            operands["row_a"] = i - 1
            command = command.replace(f"R{i}", "")
            break
    for i in range(1, 10):  # operands["row_a"], 10):
        if f"R{i}" in command:
            operands["row_b"] = i - 1
            command = command.replace(f"R{i}", "")

    # print(command)
    try:
        command = command.strip()
        if "/" in command:
            dividend = command.split("/")
            operands["scalar"] = int(dividend[0]) / int(dividend[1])
        operands["scalar"] = float(command)
    except ValueError:
        print("interpreter: no scalar found")
    # finally:
    #     print(operands)

    result_matrix = None
    if operands["function"] is matrix_operations.add:
        if operands["row_a"] is not None:
            if operands["scalar"] != 1:
                result_matrix = matrix_a.row_add_scaled(operands["row_a"], operands["scalar"], operands["row_b"])
            else:
                result_matrix = matrix_a.row_add(operands["row_a"], operands["row_b"])
        # else:
        #     result_matrix = matrix_operations.add(matrix_a, matrix_b)
    elif operands["function"] is matrix_operations.subtract:
        if operands["row_a"] is not None:
            if operands["scalar"] != 1:
                result_matrix = matrix_a.row_subtract_scaled(operands["row_a"], operands["scalar"], operands["row_b"])
            else:
                result_matrix = matrix_a.row_subtract(operands["row_a"], operands["row_b"])
        # else:
        #     result_matrix = matrix_operations.subtract(matrix_a, matrix_b)
    elif operands["function"] is matrix_operations.scale and operands["row_a"] is not None:
        result_matrix = matrix_a.row_scale(operands["scalar"], operands["row_a"])
    elif operands["function"] is matrix_operations.get_determinant:
        return matrix_a.get_determinant()
    elif operands["matrix_B"] is not None:
        result_matrix = operands["function"](matrix_a, matrix_b)
    else:
        result_matrix = operands["function"](matrix_a)

    result_matrix.display()
    return result_matrix
