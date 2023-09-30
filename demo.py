import matrix_operations

matrix.ITERATION_START = 0

m1 = matrix.Entries(entries=([1, 2, 0], [3, 4, -1], [5, 6, -2]))
m1[0][2] = 1
m2 = matrix.Identity(3)

m1.display()

if m1.transpose() == matrix.transpose(matrix=m1):
    matrix.display(matrix=m1.transpose())

if m1.get_submatrix(skipped_row=0, skipped_column=0) == matrix.get_submatrix(m1, skipped_row=0, skipped_column=0):
    matrix.display(m1.transpose())

if m1.get_determinant() == matrix.get_determinant(matrix=m1):
    print(f"{m1.determinant}\n")

if m1.inverse() == matrix.inverse(matrix=m1):
    m1.inverse().display()

if m1.scale(scalar=-1) == matrix.scale(scalar=-1, matrix=m1):
    m1.scale(-1).display()

if m1.add(matrix_added=m2) == matrix.add(matrix_a=m1, matrix_b=m2):
    m1.add(m2).display()

if m1.multiply(matrix_multiplying=m2) == matrix.multiply(matrix_a=m1, matrix_b=m2):
    mat = m1.multiply(m2)
    mat.display()

m3 = matrix.multiply(m1.transpose(), matrix.transpose(m1).inverse()).scale(-1).display()