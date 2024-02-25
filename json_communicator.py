import json
# import matrix_reconciled as matrix


def json_reader(matrix_letter):
    with open(f"matrix{matrix_letter}.json") as matrix_file:
        matrix_dict = json.loads(matrix_file.read())
        matrix_list = []
        # row = 0
        for key_row in matrix_dict:
            # row += 1
            matrix_list.append([])
            for key_column in matrix_dict[key_row]:
                matrix_list[-1].append(matrix_dict[key_row][key_column])
    # breakpoint()
    return matrix_list
    # matrix.Matrix_Being(entries=, tk_master=container_matrix_, name=matrix_letter)
