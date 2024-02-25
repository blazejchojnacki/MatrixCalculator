import tkinter

import matrix_reconciled as matrix
import json_communicator as communicator
from matrix_math import Identity
from matrix_history import history_purge
from matrix_tk_display import Matrix_Grid, Matrix_Entry
import calculator_engine
from common import selected
# selected = common.selected

step_counter = 1
undo_counter = 1


def history_undo():
    global step_counter, undo_counter, current
    undo_counter += 1
    # if undo_counter <= step_counter:
    try:
        previous_step = A.history.undo(undo_counter)
    except IndexError:
        print("end of history")
        undo_counter = 1
        previous_step = A.history.undo(undo_counter)
    finally:
        current["command"] = previous_step["command"]
        current["matrix"].entries = previous_step["matrix"]
        refresh()
        current["matrix"].history.history_append(command="undo", matrix=current["matrix"].entries)
        return


def refresh():
    global current
    for row_number in range(current["matrix"].entries.number_of_rows):
        for column_number in range(current["matrix"].entries.number_of_columns):
            if current["matrix"].entries[row_number][column_number] % 1 == 0:
                current["matrix"].entries[row_number][column_number] = int(current["matrix"].entries[row_number][column_number])
            current["matrix"].display[row_number][column_number].config(text=current["matrix"].entries[row_number][column_number])


def call_interpreter():
    global step_counter, current, selected
    current["command"] = command_line.get()
    message_label.config(text="interpreting")
    try:
        command_result = calculator_engine.command_interpreter(current["command"], matrix_a=current["matrix"])
        message_label.config(text="command applied")
        if type(command_result) is int or type(command_result) is float:
            determinant_label.config(text=command_result)
        else:
            current["matrix"].entries = command_result
            refresh()
            current["matrix"].history.history_append(current["command"], current["matrix"].entries)
            step_counter += 1
    except:
        message_label.config(text="interpreter failed interpreting")
    finally:
        selected = {
            "rowA": None,
            "rowB": None,
            "matrixA": None,
            "matrixB": None
        }


def call_operation(operation):
    command_line.delete(0, 'end')
    command_line.insert(0, operation)
    call_interpreter()


def transpose():
    call_operation("transpose")


def inverse():
    call_operation("invert")


def scale():
    call_operation(f"scale {op_entry_scale.get()}")


def determine():
    call_operation("det")
    if current["matrix"].entries.determinant % 1 == 0:
        determinant_label.config(text=f'|A| = {current["matrix"].entries.determinant}')
    else:
        determinant_label.config(text=f'|A| ≈ {round(current["matrix"].entries.determinant,4)}')


def edit_matrix():
    global current

    def save_matrix():
        for row in range(new_matrix.entries.number_of_rows):
            for column in range(new_matrix.entries.number_of_columns):
                new_matrix.entries[row][column] = float(new_matrix.display[row][column].get())
        # breakpoint()
        current["matrix"].convert(new_matrix)
        refresh()

    def add_new_row():
        # new_matrix.entries.number_of_rows += 1
        new_matrix.entries.append([0 for _ in range(new_matrix.entries.number_of_columns)])
        newer_matrix = matrix.Matrix_Editable(name="Z", entries=new_matrix.entries, tk_master=window_editor)
        new_matrix.display = newer_matrix.display
        return

    def delete_last_row():
        new_matrix.entries.pop()
        new_matrix.display.pop()
        pass

    window_editor = tkinter.Tk()
    window_editor.title("Matrix Editor")
    window_editor.minsize(width=200, height=200)
    window_editor.config(padx=10, pady=10)

    new_matrix = matrix.Matrix_Editable(name="Z", entries=current["matrix"].entries, tk_master=window_editor)
    save_button = tkinter.Button(master=window_editor, text="save", command=save_matrix)
    save_button.grid(column=20, row=20)

    new_row_button = tkinter.Button(master=window_editor, text="add row", command=add_new_row)
    new_row_button.grid(row=20, column=1)
    delete_row_button = tkinter.Button(master=window_editor, text="delete last row", command=delete_last_row)
    delete_row_button.grid(row=20, column=2)

# def please_identify(yourself):
#     if type(yourself) == Matrix_Entry:
#         print(yourself.position)
#         selected["rowA"] = yourself.position[0]
#     elif type(yourself) == Matrix_Grid:
#         print(yourself.name)
#         selected["matrixA"] = yourself.name
#
#
# def identify(yourself):
#     return lambda: please_identify(yourself)


# --- --- GUI definition --- --- #


window = tkinter.Tk()
window.title("Matrix Calculator")
window.minsize(width=700, height=600)
window.config(padx=30, pady=30)

title_label = tkinter.Label(text=">title<", relief="solid", borderwidth=1, width=70, height=2)

container_actions = tkinter.Frame(padx=10, pady=10, relief="solid", borderwidth=1)
action_undo = tkinter.Button(master=container_actions, text="undo", width=8, command=history_undo)
action_undo.grid(row=1, column=1)
action_purge = tkinter.Button(master=container_actions, text=">purge<", width=8, command=history_purge)
action_purge.grid(row=2, column=1)
action_edit = tkinter.Button(master=container_actions, text="edit", width=8, command=edit_matrix)
action_edit.grid(row=4, column=1)

# container_mode = tkinter.Frame(padx=10, relief="solid", borderwidth=1)
# chosen_mode = tkinter.IntVar()
# mode_radio_single_edit = tkinter.Radiobutton(master=container_mode, text="single matrix edition", value=1,
#                                              variable=chosen_mode, command=mode_change)
# mode_radio_single_edit.grid(row=1)
# mode_radio_single_operate = tkinter.Radiobutton(master=container_mode, text="single matrix math", value=2,
#                                                 variable=chosen_mode, command=mode_change)
# mode_radio_single_operate.grid(row=2)
# mode_radio_two_operate = tkinter.Radiobutton(master=container_mode, text="two matrices math", value=3,
#                                              variable=chosen_mode, command=mode_change)
# mode_radio_two_operate.grid(row=3)
# mode_chosen = chosen_mode.get()

container_matrices = tkinter.Frame(relief="solid", borderwidth=1, padx=20)
ruler_matrices = tkinter.Label(master=container_matrices, width=50, height=25)
ruler_matrices.grid(row=0, column=1, columnspan=4, rowspan=3)

container_matrix_A = tkinter.Frame(master=container_matrices)
container_matrix_B = tkinter.Frame(master=container_matrices)
container_matrix_A.grid(row=1, column=1)
container_matrix_B.grid(row=1, column=3)

container_operator = tkinter.Frame(borderwidth=1, relief="solid")
ruler_operator = tkinter.Label(master=container_operator, width=12, height=20)
ruler_operator.grid(row=0, column=0, rowspan=6, columnspan=2)
operator_transpose = tkinter.Button(master=container_operator, text="T", width=5, command=transpose, padx=5, pady=10)
operator_transpose.grid(row=1, column=1)
operator_inverse = tkinter.Button(master=container_operator, text="I", width=5, command=inverse, padx=5, pady=10)
operator_inverse.grid(row=2, column=1)
op_entry_scale = tkinter.Entry(master=container_operator, width=5)
op_entry_scale.insert(0, string="1")
op_entry_scale.grid(row=3, column=0)
operator_scale = tkinter.Button(master=container_operator, text="S", width=5, command=scale, padx=5, pady=10)
operator_scale.grid(row=3, column=1)
determinant_button = tkinter.Button(master=container_operator, text="det A", command=determine, width=5, padx=5, pady=10)
determinant_button.grid(row=4, column=1)
determinant_label = tkinter.Label(master=container_operator, text="|A| undefined")
# determinant_label.grid(row=5, column=0, columnspan=2)


container_command = tkinter.Frame(relief="solid")
# ruler_command = tkinter.Label(master=container_command, width=50)
# ruler_command.grid(row=0, column=1, columnspan=2)
command_line = tkinter.Entry(master=container_command, width=30)
command_line.grid(row=1, column=1)
interpret = tkinter.Button(master=container_command, text="enter", command=call_interpreter)
interpret.grid(row=1, column=2)
message_label = tkinter.Label(master=container_command, text="type a command and press the 'enter' button")
message_label.grid(row=2, column=1, columnspan=2)


# --- main grid --- #
title_label.grid(row=1, column=1, columnspan=9)
container_operator.grid(row=2, column=1)
container_matrices.grid(row=2, column=2)
container_command.grid(row=3, column=1, columnspan=2)
container_actions.grid(row=2, column=3)

# --- used values --- #

A = matrix.Matrix_Selectable(entries=communicator.json_reader("A"), tk_master=container_matrix_A, name='A')
B = matrix.Matrix_Selectable(entries=Identity(3), tk_master=container_matrix_B, name='B')

# A.display.brackets.configure(command=identify(A.display))
# for row_number in range(A.entries.number_of_rows):
#     for column_number in range(A.entries.number_of_columns):
#         A.display[row_number][column_number].configure(command=identify(yourself=A.display[row_number][column_number]))

current = {
    "command": "start",
    "matrix": A,
    "message": "type a command and press the 'enter' button",
}

window.mainloop()
