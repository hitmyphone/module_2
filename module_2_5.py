def get_matrix (n,m,value):
    structure = [n,m,value]
    matrix = []
    for i in range(n):
        mat1 = []
        matrix.append(mat1)
        for j in range(m):
            mat1.append(value)
    return matrix

mat = get_matrix(4,2,13)
print(mat)




