import tkinter
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


def mode_change():
    global mode_radio_grid
    mode_radio_single_edit.grid(row=mode_radio_grid[0] - 1, column=mode_radio_grid[1], columnspan=2)
    pass


def call_interpreter():
    global current_command, current_matrix
    current_command = command_line.get()
    command_result = command_interpreter(current_command, matrix_a=current_matrix)
    if command_result is int or command_result is float:
        determinant_label.config(text=command_result)
    else:
        current_matrix = command_result
        refresh()


current_command = ""

m1 = matrix_operations.Entries(entries=([1, 2, 1], [3, 4, -1], [5, 6, -2]))
m2 = matrix_operations.Identity(6)
current_matrix = m1

window = tkinter.Tk()
window.title("Matrix Calculator")
window.minsize(width=600, height=500)
window.config(padx=50, pady=50)

title_label = tkinter.Label(text=">title<", padx=10, relief="solid", borderwidth=1)

#
# matrix_locked = tkinter.IntVar()
# button_lock = tkinter.Checkbutton(text="Lock matrix", variable=matrix_locked)

container_mode = tkinter.Frame(padx=10, relief="solid", borderwidth=1)
chosen_mode = tkinter.IntVar()
mode_radio_single_edit = tkinter.Radiobutton(master=container_mode, text="single matrix edition", value=1,
                                             variable=chosen_mode, command=mode_change)
mode_radio_single_edit.grid(row=1)
mode_radio_single_operate = tkinter.Radiobutton(master=container_mode, text="single matrix operations", value=2,
                                                variable=chosen_mode, command=mode_change)
mode_radio_single_operate.grid(row=2)
mode_radio_two_operate = tkinter.Radiobutton(master=container_mode, text="two matrices operations", value=3,
                                             variable=chosen_mode, command=mode_change)
mode_radio_two_operate.grid(row=3)
mode_chosen = chosen_mode.get()

container_matrices = tkinter.Frame(relief="solid", borderwidth=1, padx=10)
container_matrix_A = tkinter.Frame(master=container_matrices, width=80)
matrix_A_interface = Matrix_Grid(m1, master=container_matrix_A)
space_label = tkinter.Label(master=container_matrices, text=" ", width=1)
container_matrix_B = tkinter.Frame(master=container_matrices)
matrix_B_interface = Matrix_Grid(m2, master=container_matrix_B)
container_matrix_A.grid(row=1, column=1)
space_label.grid(row=1, column=2)
container_matrix_B.grid(row=1, column=3)
# space_label2 = tkinter.Label(master=container_matrices, text=" ", width=1)

container_operator = tkinter.Frame(width=5, borderwidth=1, relief="solid")
operator_transpose = tkinter.Button(master=container_operator, text="T", width=5, command=transpose)
operator_transpose.grid(row=1, column=1)
operator_inverse = tkinter.Button(master=container_operator, text="I", width=5, command=inverse)
operator_inverse.grid(row=2, column=1)
operator_scale = tkinter.Button(master=container_operator, text="S", width=5, command=scale)
operator_scale.grid(row=3, column=1)
determinant_button = tkinter.Button(master=container_operator, text="det A", command=determine)
determinant_button.grid(row=4, column=1)
determinant_label = tkinter.Label(master=container_operator, text="undefined")
determinant_label.grid(row=5, column=1)

container_command = tkinter.Frame()
command_line = tkinter.Entry(master=container_command, width=30)
command_line.grid(row=1, column=1)
interpret = tkinter.Button(master=container_command, text="enter", command=call_interpreter)
interpret.grid(row=1, column=2)


# --- main grid --- #
title_label.grid(row=1, column=1, columnspan=9)
container_operator.grid(row=2, column=1)
container_matrices.grid(row=2, column=2)
container_command.grid(row=3, column=1, columnspan=2)
container_mode.grid(row=2, column=3)

window.mainloop()
