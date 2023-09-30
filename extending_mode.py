import tkinter

window = tkinter.Tk()
window.title("Matrix Calculator")
window.minsize(width=500, height=500)

title_label = tkinter.Label(text=">title<")

# def lock_matrix():
#     global matrix_locked
#     matrix_locked = True

matrix_locked = tkinter.IntVar()
button_lock = tkinter.Checkbutton(text="Lock matrix", variable=matrix_locked)


def select_me():
    pass


grid_matrix_begin_row = 2
grid_matrix_begin_column = 2
grid_matrix_end_row = 2
grid_matrix_end_column = 2
grid_matrix = []


def extend_matrix(number_of_rows=1, number_of_columns=1):
    global grid_matrix_end_row, grid_matrix_end_column
    for row_number in range(number_of_rows):
        grid_matrix.append([])
        for column_number in range(number_of_columns):
            grid_matrix[row_number].append(tkinter.Button(text="0", command=select_me))
            grid_matrix[row_number][column_number].grid(row=grid_matrix_begin_row + row_number,
                                               column=grid_matrix_begin_column + column_number)
    grid_matrix_end_row = len(grid_matrix) + 1
    grid_matrix_end_column = len(grid_matrix[0]) + 1


extender = tkinter.Button(text="+", command=extend_matrix)
extender.grid(row=grid_matrix_end_row, column=grid_matrix_end_column)

title_label.grid(row=1, column=1)
button_lock.grid(row=1, column=2)

window.mainloop()