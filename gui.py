from tkinter import Label, Frame
import matrix_operations


class Matrix_Entry(Label):  # Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = (0, 0)
        self.entry = None


class Matrix_Grid(list):
    ENTRY_WIDTH = 4

    def __init__(self, entries, master):
        super().__init__()
        self.entries = entries
        self.brackets = Label(master=master, text="", width=0 + (self.ENTRY_WIDTH + 2) * self.entries.number_of_columns,
                              height=-1 + (self.ENTRY_WIDTH - 2) * self.entries.number_of_rows, borderwidth=1, relief="solid")
        self.brackets.grid(row=2, column=1, columnspan=3)
        self.container = Frame(master=master)
        self.container.grid(row=1, column=2, rowspan=3)
        for row_number in range(self.entries.number_of_rows):
            self.append([])
            for column_number in range(self.entries.number_of_columns):
                self[row_number].append(Matrix_Entry(master=self.container, width=self.ENTRY_WIDTH,
                                        padx=4, pady=4, text=self.entries[row_number][column_number]))
                self[row_number][column_number].position = (row_number, column_number)
                self[row_number][column_number].entry = self.entries[row_number][column_number]
                self[row_number][column_number].grid(row=row_number, column=column_number)


# -------------------------------------#


def command_interpreter(command, matrix_a=None, matrix_b=None):
    operands = {
        "matrix_A": None,
        "matrix_B": None,
        "row_a": None,
        "row_b": None,
        "scalar": 1,
        "function": None,
    }

    operation_dict = {}

    if matrix_a is not None:
        operands["matrix_A"] = matrix_a
        operation_dict = matrix_operations.operation_matrix_dict
    if matrix_b is not None:
        operands["matrix_B"] = matrix_b
        operation_dict = matrix_operations.operation_matrices_dict

    for i in range(1, 10):
        if f"R{i}" in command:
            operands["row_a"] = i - 1
            command = command.replace(f"R{i}", "")
            operation_dict = matrix_operations.operation_row_dict
            break
    for i in range(1, 10):  # operands["row_a"], 10):
        if f"R{i}" in command:
            operands["row_b"] = i - 1
            command = command.replace(f"R{i}", "")

    for key in operation_dict:
        if key in command:
            operands["function"] = operation_dict[key]
            command = command.replace(key, "")
    try:
        command = command.strip()
        if "/" in command:
            dividend = command.split("/")
            operands["scalar"] = int(dividend[0]) / int(dividend[1])
        operands["scalar"] = float(command)
    except ValueError:
        pass
        # print("interpreter: no scalar found")

    result_matrix = None
    if operands["function"] is matrix_operations.row_add:
        if operands["scalar"] != 1:
            result_matrix = matrix_a.row_add_scaled(operands["row_a"], operands["scalar"], operands["row_b"])
        else:
            result_matrix = matrix_a.row_add(operands["row_a"], operands["row_b"])
    elif operands["function"] is matrix_operations.row_subtract:
        if operands["scalar"] != 1:
            result_matrix = matrix_a.row_subtract_scaled(operands["row_a"], operands["scalar"], operands["row_b"])
        else:
            result_matrix = matrix_a.row_subtract(operands["row_a"], operands["row_b"])
    elif operands["function"] is matrix_operations.row_scale:
        result_matrix = matrix_a.row_scale(operands["scalar"], operands["row_a"])
    elif operands["function"] is matrix_operations.get_determinant:
        return matrix_a.get_determinant()
    elif operands["matrix_B"] is not None:  # operands["function"] in matrix_operations.operation_matrices_dict:
        result_matrix = operands["function"](matrix_a, matrix_b)
    elif operands["function"] is matrix_operations.scale:
        result_matrix = matrix_a.scale(operands["scalar"])
    else:
        result_matrix = operands["function"](matrix_a)

    # result_matrix.display()
    return result_matrix
