import matrix_math


def command_interpreter(command, matrix_a=None, matrix_b=None):

    # operands = {
    #     "matrix_A": None,
    #     "matrix_B": None,
    #     "row_a": None,
    #     "row_b": None,
    #     "scalar": 1,
    #     "function": None,
    # }
    
    inter_mat_a = None
    inter_mat_b = None
    inter_row_a = None
    inter_row_b = None
    inter_scalar = 1
    inter_function = None
    result_matrix = None

    operation_dict = {}

    if matrix_a is not None:
        inter_mat_a = matrix_a.entries
        operation_dict = matrix_math.operation_matrix_dict
    if matrix_b is not None:
        inter_mat_b = matrix_b.entries
        operation_dict = matrix_math.operation_matrices_dict

    for i in range(1, 10):
        if f"R{i}" in command:
            inter_row_a = i - 1
            command = command.replace(f"R{i}", "")
            operation_dict = matrix_math.operation_row_dict
            break
    for i in range(1, 10):
        if f"R{i}" in command:
            inter_row_b = i - 1
            command = command.replace(f"R{i}", "")

    for key in operation_dict:
        if key in command:
            inter_function = operation_dict[key]
            command = command.replace(key, "")
    try:
        command = command.strip()
        if "/" in command:
            dividend = command.split("/")
            inter_scalar = int(dividend[0]) / int(dividend[1])
        inter_scalar = float(command)
    except ValueError:
        pass

    if inter_function is matrix_math.row_add:
        if inter_scalar != 1:
            result_matrix = inter_mat_a.row_add_scaled(inter_row_a, inter_scalar, inter_row_b)
        else:
            result_matrix = inter_mat_a.row_add(inter_row_a, inter_row_b)
    elif inter_function is matrix_math.row_subtract:
        if inter_scalar != 1:
            result_matrix = inter_mat_a.row_subtract_scaled(inter_row_a, inter_scalar, inter_row_b)
        else:
            result_matrix = inter_mat_a.row_subtract(inter_row_a, inter_row_b)
    elif inter_function is matrix_math.row_scale:
        result_matrix = inter_mat_a.row_scale(inter_scalar, inter_row_a)
    elif inter_function is matrix_math.get_determinant:
        return inter_mat_a.get_determinant()
    elif inter_mat_b is not None:
        result_matrix = inter_function(inter_mat_a, inter_mat_b)
    elif inter_function is matrix_math.scale:
        result_matrix = inter_mat_a.scale(inter_scalar)
    else:
        # breakpoint()
        result_matrix = inter_function(inter_mat_a)
    return result_matrix
