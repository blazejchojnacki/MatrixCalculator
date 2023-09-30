import tkinter
# from tkinter import messagebox
from gui import Matrix_Grid, command_interpreter
import matrix_operations


def refresh():
    global current_matrix
    for row_number in range(current_matrix.number_of_rows):
        for column_number in range(current_matrix.number_of_columns):
            if current_matrix[row_number][column_number] % 1 == 0:
                current_matrix[row_number][column_number] = int(current_matrix[row_number][column_number])
            matrix_A_interface[row_number][column_number].config(text=current_matrix[row_number][column_number])


def call_operation(operation):
    global current_matrix
    command_line.delete(0, 'end')
    command_line.insert(0, operation)
    current_matrix = matrix_operations.operation_dict[operation](current_matrix)
    refresh()


def transpose():
    call_operation("transpose")
    # current_matrix = matrix


def inverse():
    call_operation("invert")


def scale():
    call_operation("scale")


def determine():
    call_operation("det")
    determinant_label.config(text=current_matrix.determinant)


# def mode_change():
#     global mode_radio_grid
#     mode_radio_single_edit.grid(row=mode_radio_grid[0] - 1, column=mode_radio_grid[1], columnspan=2)
#     pass


def call_interpreter():
    global current_command, current_matrix
    current_command = command_line.get()
    command_result = command_interpreter(current_command, matrix_a=current_matrix)
    # breakpoint()
    if command_result is int or command_result is float:
        determinant_label.config(text=command_result)
    # elif command_result is matrix_operations.Entries:
    else:
        current_matrix = command_result
        refresh()
        # for row_number in range(current_matrix.number_of_rows):
        #     for column_number in range(current_matrix.number_of_columns):
        #         matrix_A_interface[row_number][column_number].config(text=current_matrix[row_number][column_number])


current_command = ""

m1 = matrix_operations.Entries(entries=([1, 2, 1], [3, 4, -1], [5, 6, -2]))
m2 = matrix_operations.Identity(3)
current_matrix = m1

window = tkinter.Tk()
window.title("Matrix Calculator")
window.minsize(width=600, height=500)
window.config(padx=50, pady=50)

title_label = tkinter.Label(text=">title<")

matrix_locked = tkinter.IntVar()
button_lock = tkinter.Checkbutton(text="Lock matrix", variable=matrix_locked)

# chosen_mode = tkinter.IntVar()
# mode_radio_single_edit = tkinter.Radiobutton(text="single matrix edition", value=1,
#                                              variable=chosen_mode, command=mode_change)
# mode_radio_single_operate = tkinter.Radiobutton(text="single matrix operations", value=2,
#                                                 variable=chosen_mode, command=mode_change)
# mode_radio_two_operate = tkinter.Radiobutton(text="two matrices operations", value=3,
#                                              variable=chosen_mode, command=mode_change)
# mode_chosen = chosen_mode.get()

matrix_A_interface = Matrix_Grid(m1)
space_label = tkinter.Label(text=" ", width=1)
matrix_B_interface = Matrix_Grid(m2)
space_label2 = tkinter.Label(text=" ", width=1)
operator_transpose = tkinter.Button(text="T", width=5, command=transpose)
operator_inverse = tkinter.Button(text="I", width=5, command=inverse)
operator_scale = tkinter.Button(text="S", width=5, command=scale)
# operator_frame = tkinter.Frame(width=10, borderwidth=1)
command_line = tkinter.Entry(width=50)
interpret = tkinter.Button(text="enter", command=call_interpreter)
determinant_button = tkinter.Button(text="det A", command=determine)
determinant_label = tkinter.Label(text="undefined")

# --- GRID --- #

# title_label.grid(row=1, column=1, columnspan=9)
# button_lock.grid(row=1, column=11, columnspan=3)
# mode_radio_grid = (2, 15)
# mode_radio_single_edit.grid(row=mode_radio_grid[0], column=mode_radio_grid[1], columnspan=2)
# mode_radio_single_operate.grid(row=mode_radio_grid[0] + 1, column=mode_radio_grid[1], columnspan=2)
# mode_radio_two_operate.grid(row=mode_radio_grid[0] + 2, column=mode_radio_grid[1], columnspan=2)
matrix_A_grid = (3, 3)
# matrix_B_grid = (3, matrix_A_grid[1] + m1.number_of_columns + 3)
matrix_A_interface.place(matrix_A_grid[0], matrix_A_grid[1])
# matrix_B_interface.place(matrix_B_grid[0], matrix_B_grid[1])
space_label.grid(row=2, column=matrix_A_grid[0] + matrix_A_interface.entries.number_of_columns + 2, rowspan=2)
space_label2.grid(row=2, column=2)
# operator_grid = (3, 1)
# operator_transpose.grid(row=operator_grid[0], column=operator_grid[1])
# operator_inverse.grid(row=operator_grid[0] + 1, column=operator_grid[1])
# operator_scale.grid(row=operator_grid[0] + 2, column=operator_grid[1])
# operator_frame.grid(row=operator_grid[0], column=operator_grid[1], rowspan=3)
# interpret.grid(row=10, column=1)
# command_line.grid(row=10, column=2, columnspan=10)
# determinant_button.grid(row=operator_grid[0] + 3, column=operator_grid[1])
# determinant_label.grid(row=matrix_A_grid[0] + m1.number_of_rows + 2, column=matrix_A_grid[1], columnspan=2)

window.mainloop()
