ITERATION_START = 0


class Entries(list):
    """creates a free-form matrix based on given entries"""
    def __init__(self, entries):
        super().__init__()
        self.number_of_rows = len(entries)
        self.number_of_columns = len(entries[0])
        for row_number in range(self.number_of_rows):  # range(ITER..., ITER... + self.numb...)
            self.append(entries[row_number])
        self.determinant = self.get_determinant()
    # def input_from_console(self):
    # def input_from_file(self, filepath):

    def display(self):
        """returns the matrix after printing it, formatted"""
        matrix = display(self)
        return matrix

    def transpose(self):
        """ returns the matrix, transposed"""
        matrix = transpose(self)
        return matrix

    def get_submatrix(self, skipped_row, skipped_column):
        """ returns the submatrix of the matrix, given the skipped row and column """
        matrix = get_submatrix(self, skipped_row, skipped_column)
        return matrix

    def get_determinant(self):
        """ returns the determinant of the matrix"""
        self.determinant = get_determinant(self)
        return self.determinant

    def inverse(self):
        """ returns the inverse of the matrix """
        matrix = inverse(self)
        return matrix

    def scale(self, scalar):
        """ returns the matrix multiplied by a given scalar """
        matrix = scale(scalar, self)
        return matrix

    def add(self, matrix_added):
        """ returns the sum of the matrix and a given matrix """
        matrix_sum = add(self, matrix_added)
        return matrix_sum

    def subtract(self, matrix_subtracting):
        """ returns the difference-matrix between the matrix and another given one """
        matrix_difference = subtract(self, matrix_subtracting)
        return matrix_difference

    def multiply(self, matrix_multiplying):
        """ returns the product of the matrix and a given matrix """
        matrix_product = multiply(self, matrix_multiplying)
        return matrix_product

    def row_permute(self, permuted_row_1, permuted_row_2):
        """ returns the matrix where two given rows have been permuted """
        matrix_permuted = row_permute(self, permuted_row_1, permuted_row_2)
        return matrix_permuted

    def row_scale(self, scalar, row):
        """ returns the matrix where a given row have been multiplied by a scalar """
        matrix_scaled = row_scale(self, scalar, row)
        return matrix_scaled

    def row_add(self, added_row_modified, added_row_idle):
        """ returns the matrix where a given row has been added to another given row """
        matrix_added = row_add(self, added_row_modified, added_row_idle)
        return matrix_added

    def row_subtract(self, row_modified, subtracted_row_idle):
        """ returns the given matrix where a given row has been subtracted to another given row """
        matrix_result = row_subtract(self, row_modified, subtracted_row_idle)
        return matrix_result

    def row_add_scaled(self, row_modified, scalar, added_row_idle):
        """ returns the matrix where a given row has been multiplied by a given scalar
         and added to another given row """
        matrix_result = row_add_scaled(self, row_modified, scalar, added_row_idle)
        return matrix_result

    def row_subtract_scaled(self, row_modified, scalar, subtracted_row_idle):
        """ returns the given matrix where a given row has been multiplied by a given scalar
         and subtracted to another given row """
        matrix_result = row_subtract_scaled(self, row_modified, scalar, subtracted_row_idle)
        return matrix_result


class Identity(Entries):
    """ creates a square identity matrix of given column or row length """
    def __init__(self, size):
        self.number_of_rows = int(size)
        self.number_of_columns = int(size)
        entries = []
        for row_number in range(self.number_of_rows):
            entries.append([])
            for column_number in range(self.number_of_columns):
                if row_number == column_number:
                    entries[row_number].append(1)
                else:
                    entries[row_number].append(0)
        super().__init__(entries)
        self.determinant = 1


def stringify(matrix):
    """returns the multiline string representing the matrix"""
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    string_matrix = ""
    for row_number in range(number_of_rows):
        string_matrix += "|\t"
        for column_number in range(number_of_columns):
            string_matrix += f"{matrix[row_number][column_number]}\t"
        string_matrix += "|\n"
    string_matrix += "\n"
    return string_matrix


def read_string(string_matrix):
    string_matrix = string_matrix[0:-2]
    string_matrix = string_matrix.split("\n")
    number_of_rows = len(string_matrix)
    result_matrix = []
    for row_number in range(number_of_rows):
        string_matrix[row_number] = string_matrix[row_number].strip("|\t")
        string_matrix[row_number] = string_matrix[row_number].split("\t")
        # number_of_columns = len(string_matrix[0])
        result_matrix.append([float(entry) for entry in string_matrix[row_number]])
    return Entries(result_matrix)


def display(matrix):
    """ returns a given matrix after printing it to the console """
    # number_of_rows = len(matrix)
    # number_of_columns = len(matrix[0])
    # for row_number in range(number_of_rows):
    #     line = "|\t"
    #     for column_number in range(number_of_columns):
    #         line += f"{matrix[row_number][column_number]}\t"
    #     print(f"{line}|")
    print(stringify(matrix))
    return matrix


def transpose(matrix):
    """ returns the given matrix transposed """
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    transposed = []
    for column_number in range(number_of_columns):
        transposed.append([])
        for row_number in range(number_of_rows):
            transposed[column_number].append(matrix[row_number][column_number])
    transposed_matrix = Entries(transposed)
    return transposed_matrix


def get_submatrix(matrix, skipped_row, skipped_column):
    """ returns the submatrix of a provided matrix, given the skipped row and column """
    number_of_rows = len(matrix) - 1
    number_of_columns = len(matrix[0]) - 1
    sub_entries = []
    skip_row = 0
    for row_number in range(number_of_rows):
        if row_number + ITERATION_START == skipped_row:
            skip_row = 1
        sub_entries.append([])
        skip_column = 0
        for column_number in range(number_of_columns):
            if column_number + ITERATION_START == skipped_column:
                skip_column = 1
            sub_entries[row_number].append(matrix[row_number + skip_row][column_number + skip_column])
    submatrix = Entries(sub_entries)
    return submatrix


def get_determinant(matrix):
    """ returns the determinant of a given matrix """
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    if number_of_rows == number_of_columns:
        if number_of_rows == 1:
            determinant = matrix[0][0]
        else:
            determinant = 0
            for column_number in range(number_of_columns):
                submatrix = get_submatrix(matrix, 0 + ITERATION_START, column_number + ITERATION_START)
                determinant += (-1) ** column_number * matrix[0][column_number] * get_determinant(submatrix)
        return determinant


def inverse(matrix):
    """ returns the inverse of a given matrix """
    determinant = get_determinant(matrix)
    if determinant != 0:
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])
        inverted = []
        for row_number in range(number_of_rows):
            inverted.append([])
            for column_number in range(number_of_columns):
                submatrix = get_submatrix(matrix, row_number + ITERATION_START, column_number + ITERATION_START)
                inverted[row_number].append(get_determinant(submatrix) / determinant)
                if inverted[row_number][column_number] % 1 == 0:
                    inverted[row_number][column_number] = int(inverted[row_number][column_number])
                inverted[row_number][column_number] *= (-1) ** (row_number + column_number)
        inverse_matrix = transpose(Entries(inverted))
        return inverse_matrix


def scale(scalar, matrix):
    """ returns the given matrix multiplied by a given scalar """
    number_of_rows = len(matrix)
    scaled = []
    for row_number in range(number_of_rows):
        row = matrix[row_number]
        scaled.append([term * scalar for term in row])
    scaled_matrix = Entries(scaled)
    return scaled_matrix


def add(matrix_a, matrix_b):
    """ returns the sum-matrix of two given matrices """
    number_of_rows_a = len(matrix_a)
    number_of_columns_a = len(matrix_a[0])
    number_of_rows_b = len(matrix_b)
    number_of_columns_b = len(matrix_b[0])
    if number_of_rows_a == number_of_rows_b and number_of_columns_a == number_of_columns_b:
        result = []
        for row_number in range(number_of_rows_a):
            result.append([])
            for column_number in range(number_of_columns_a):
                result[row_number].append(matrix_a[row_number][column_number] + matrix_b[row_number][column_number])
        sum_matrix = Entries(result)
        return sum_matrix


def subtract(matrix_a, matrix_b):
    """ returns the difference-matrix of two given matrices """
    difference_matrix = add(matrix_a, scale(-1, matrix_b))
    return difference_matrix


def multiply(matrix_a, matrix_b):
    """ returns the product-matrix of two given matrices """
    number_of_rows_a = len(matrix_a)
    number_of_columns_a = len(matrix_a[0])
    number_of_rows_b = len(matrix_b)
    number_of_columns_b = len(matrix_b[0])
    if number_of_columns_a == number_of_rows_b:
        product = []
        for row_number_a in range(number_of_rows_a):
            product.append([])
            for column_number_b in range(number_of_columns_b):
                product[row_number_a].append(0)
                for column_number_a in range(number_of_columns_a):
                    row_number_b = column_number_a
                    product[row_number_a][column_number_b] += (matrix_a[row_number_a][column_number_a]
                                                               * matrix_b[row_number_b][column_number_b])
        product_matrix = Entries(product)
        return product_matrix


# --- elementary row operations --- #

def row_permute(matrix, permuted_row_1, permuted_row_2):
    """ returns a given matrix where two given rows have been permuted """
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    permuted = []
    for row_number in range(number_of_rows):
        permuted.append([])
        permutation = row_number
        if row_number == permuted_row_1:
            permutation = permuted_row_2
        elif row_number == permuted_row_2:
            permutation = permuted_row_1
        for column_number in range(number_of_columns):
            permuted[row_number].append(matrix[permutation][column_number])
    permuted_matrix = Entries(permuted)
    return permuted_matrix


def row_scale(matrix, scalar, row):
    """ returns a given matrix where a given rows have been multiplied by a given scalar """
    number_of_rows = len(matrix)
    scaled = []
    for row_number in range(number_of_rows):
        if row_number == row:
            scaled.append([entry * scalar for entry in matrix[row_number]])
        else:
            scaled.append(matrix[row_number])
    scaled_matrix = Entries(scaled)
    return scaled_matrix


def row_add(matrix, row_modified, added_row_idle):
    """ returns a given matrix where a given row has been added to another given row """
    added_matrix = row_add_scaled(matrix, row_modified, 1, added_row_idle)
    return added_matrix


def row_subtract(matrix, row_modified, subtracted_row_idle):
    """ returns the given matrix where a given row has been subtracted to another given row """
    result_matrix = row_add_scaled(matrix, row_modified, -1, subtracted_row_idle)
    return result_matrix


def row_add_scaled(matrix, row_modified, scalar, added_row_idle):
    """ returns the given matrix where a given row has been multiplied by a given scalar
     and added to another given row """
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    matrix_scaled = scale(scalar, matrix)
    added = []
    for row_number in range(number_of_rows):
        added.append([])
        for column_number in range(number_of_columns):
            if row_number == row_modified:
                added[row_number].append(matrix[row_modified][column_number]
                                         + matrix_scaled[added_row_idle][column_number])
            else:
                added[row_number].append(matrix[row_number][column_number])
    result_matrix = Entries(added)
    return result_matrix


def row_subtract_scaled(matrix, row_modified, scalar, subtracted_row_idle):
    """ returns the given matrix where a given row has been multiplied by a given scalar
     and subtracted to another given row """
    result_matrix = row_add_scaled(matrix, row_modified, -1 * scalar, subtracted_row_idle)
    return result_matrix


# --- dictionary for referencing function --- #
operation_dict = {
    "transpose": transpose,
    "invert": inverse,
    "det": get_determinant,
    "add": add,
    "+": add,
    "subtract": subtract,
    "-": subtract,
    "scale": scale,
}

operation_row_dict = {
    "add": row_add,
    "+": row_add,
    "subtract": row_subtract,
    "-": row_subtract,
    "scale": row_scale,
    "*": row_scale,
    "x": row_scale,
}

operation_matrix_dict = {
    "transpose": transpose,
    "invert": inverse,
    "scale": scale,
    "det": get_determinant,
    "|": get_determinant,
}

operation_matrices_dict = {
    "add": add,
    "+": add,
    "subtract": subtract,
    "-": subtract,
    "multiply": multiply,
    "*": multiply,
    "x": multiply,
}
