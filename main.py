import tkinter
from gui import Matrix_Grid, command_interpreter
import matrix_operations
import history_engine
# def edit_entry()
step_counter = 1


def history_undo():
    global step_counter, current_command, current_matrix

    # undo_counter += 1
    undo_matrix = matrix_A_history.undo(step_counter)  # undo_counter)
    for key in undo_matrix:
        current_command = key
        current_matrix = undo_matrix[key]
    refresh()


def refresh():
    global current_matrix
    for row_number in range(current_matrix.number_of_rows):
        for column_number in range(current_matrix.number_of_columns):
            if current_matrix[row_number][column_number] % 1 == 0:
                current_matrix[row_number][column_number] = int(current_matrix[row_number][column_number])
            matrix_A_interface[row_number][column_number].config(text=current_matrix[row_number][column_number])


def call_interpreter():
    global step_counter, current_command, current_matrix
    current_command = command_line.get()
    try:
        command_result = command_interpreter(current_command, matrix_a=current_matrix)
        message_label.config(text="command applied")
        if type(command_result) is int or type(command_result) is float:
            determinant_label.config(text=command_result)
        else:
            current_matrix = command_result
            refresh()
            matrix_A_history.history_append(current_command, current_matrix)
            step_counter += 1
    except:
        message_label.config(text="command unrecognized")


def call_operation(operation):
    global current_matrix
    command_line.delete(0, 'end')
    command_line.insert(0, operation)
    call_interpreter()
    # result = matrix_operations.operation_dict[operation](current_matrix)
    # if result is not int and result is not float:
    #     current_matrix = result
    #     breakpoint()
    #     refresh()


def transpose():
    call_operation("transpose")


def inverse():
    call_operation("invert")


def scale():
    call_operation("scale")


def determine():
    call_operation("det")
    determinant_label.config(text=current_matrix.determinant)


def mode_change():
    history_undo()
    # print(matrix_A_history.history_read())
    # matrix_operations.read_string(matrix_operations.stringify(m1)).display()
    # history_engine.history_purge()
    pass


current_command = ""

m1 = matrix_operations.Entries(entries=([1, 2, 1], [3, 4, -1], [5, 6, -2]))
matrix_A_history = history_engine.Recaller()
m2 = matrix_operations.Identity(2)
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
space_label2 = tkinter.Label(master=container_matrices, text=" ", width=1)
container_matrix_A.grid(row=1, column=1)
space_label.grid(row=1, column=2)
container_matrix_B.grid(row=1, column=3)
space_label2.grid(row=1, column=4)

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
message_label = tkinter.Label(master=container_command, text="type a command and press the enter button")
message_label.grid(row=2, column=1, columnspan=2)


# --- main grid --- #
title_label.grid(row=1, column=1, columnspan=9)
container_operator.grid(row=2, column=1)
container_matrices.grid(row=2, column=2)
container_command.grid(row=3, column=1, columnspan=2)
container_mode.grid(row=2, column=3)

window.mainloop()
