# for each_row in range(self.number_of_rows):
#     for each_column in range(self.number_of_columns):


class Matrix:
    entries = []
    size = (0, 0)

    def __init__(self, entries=None, identity_size=0):
        if identity_size > 0:
            for each_row in range(identity_size):
                self.entries.append([])
                for each_column in range(identity_size):
                    if each_row == each_column:
                        self.entries[each_row].append(1)
                    else:
                        self.entries[each_row].append(0)
        elif entries is None:
            self.entries = [[0]]
        self.number_of_rows = len(self.entries)
        self.number_of_columns = len(self.entries[0])
        self.size = (self.number_of_rows, self.number_of_columns)
        self.determinant = "det undefined"

    def display(self, entries=None):
        if entries is None:
            entries = self.entries
        row_length = len(entries[0])
        column_height = len(entries)
        for each_row in range(column_height):
            line = "|\t"
            for each_column in range(row_length):
                line += f"{entries[each_row][each_column]}\t"
            print(f"{line}|")
        print()
        return self

    def transpose(self, entries=None):
        if entries is None:
            entries = self.entries
        new_entries = []
        row_length = len(entries[0])
        column_height = len(entries)
        for each_column in range(row_length):
            new_entries.append([])
            for each_row in range(column_height):
                new_entries[each_column].append(entries[each_row][each_column])
        # self.entries = new_entries
        # self.number_of_columns = len(self.entries[0])
        # self.number_of_rows = len(self.entries)
        # self.size = (self.number_of_rows, self.number_of_columns)
        return new_entries  # self

    def get_submatrix(self, entries=None, eliminated_row=0, eliminated_column=0):
        # submatrix = Matrix(self.number_of_rows - 1, self.number_of_columns - 1)
        if entries is None:
            entries = self.entries
        row_length = len(entries[0]) - 1
        column_height = len(entries) - 1
        submatrix = []
        # for each_row in range(self.number_of_rows - 1):
        #     submatrix.append([])
        #     for each_column in range(self.number_of_columns - 1):
        #         submatrix[each_row].append(0)
        skip_row = 0
        skip_column = 0
        for each_row in range(column_height):
            submatrix.append([])
            if each_row == eliminated_row:
                skip_row = 1
                # each_row += 1
            for each_column in range(row_length):
                if each_column == eliminated_column:
                    # each_column += 1
                    skip_column = 1
                submatrix[each_row].append(entries[each_row + skip_row][each_column + skip_column])
        # self.entries = submatrix
        # self.number_of_columns = len(self.entries[0])
        # self.number_of_rows = len(self.entries)
        # self.size = (self.number_of_rows, self.number_of_columns)
        return submatrix  # self

    def get_determinant(self, entries=None):
        if entries is None:
            entries = self.entries
        row_length = len(entries[0])
        column_height = len(entries)
        # if self.number_of_rows == self.number_of_columns:
        #     if self.number_of_rows == 1:
        if row_length == column_height:
            if row_length == 1:
                determinant = entries[0][0]
            else:
                determinant = 0
                # for each_row in range(self.number_of_rows):
                for each_column in range(row_length):
                    submatrix = self.get_submatrix(entries, eliminated_row=0, eliminated_column=each_column)
                    determinant += ((-1) ** each_column * entries[0][each_column]
                                    * self.get_determinant(entries=submatrix))
                    # breakpoint()
            return determinant

    def invert(self, entries=None):
        if entries is None:
            entries = self.entries
        if self.get_determinant(entries) != 0:
            inverse = []
            row_length = len(entries[0])
            column_height = len(entries)
            for each_row in range(self.number_of_rows):
                inverse.append([])
                for each_column in range(self.number_of_columns):
                    inverse[each_row].append(0)
            # breakpoint()
            for each_row in range(column_height):
                for each_column in range(row_length):
                    minor = self.get_submatrix(entries=entries, eliminated_row=each_row, eliminated_column=each_column)
                    inverse[each_row][each_column] = self.get_determinant(entries=minor)
                    # print(self.get_submatrix(each_row, each_column).display().get_determinant())
                    inverse[each_row][each_column] *= (-1) ** (each_row + each_column)
                    # inverse.display()
                    inverse[each_row][each_column] /= self.get_determinant()
                    # inverse.display()
                    # breakpoint()
            # self.entries = entries
            return self.transpose(entries)
    # def input_from_console(self):
    # def input_from_file(self, filepath):


def add(matrix1=Matrix(2, 2), matrix2=Matrix(2, 2)):
    if matrix1.size == matrix2.size:
        result = Matrix(matrix1.number_of_rows, matrix1.number_of_columns)
        for each_row in range(matrix1.number_of_rows):
            for each_column in range(matrix1.number_of_columns):
                result.entries[each_row][each_column] = (matrix1.entries[each_row][each_column]
                                                         + matrix2.entries[each_row][each_column])
        return result
    # else:
    # return


def subtract(matrix1=Matrix(2, 2), matrix2=Matrix(2, 2)):
    if matrix1.size == matrix2.size:
        result = Matrix(matrix1.number_of_rows, matrix1.number_of_columns)
        for each_row in range(matrix1.number_of_rows):
            for each_column in range(matrix1.number_of_columns):
                result.entries[each_row][each_column] = (matrix1.entries[each_row][each_column]
                                                         - matrix2.entries[each_row][each_column])
        return result


def multiply(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        # result = Matrix(matrix1.number_of_rows, matrix2.number_of_columns)
        product_entries = []
        for each_row1 in range(len(matrix1)):
            product_entries.append([])
            for each_column2 in range(len(matrix2[0])):
                # should not be needed, but somehow gets the result from previous operation:
                # product_entries[each_row1][each_column2] = 0
                product_entries[each_row1].append(0)
                for each_column1 in range(len(matrix1[0])):  # == each_row2
                    product_entries[each_row1][each_column2] += (matrix1[each_row1][each_column1]
                                                                 * matrix2[each_column1][each_column2])
                    # breakpoint()
        result = Matrix(product_entries)
        return result
