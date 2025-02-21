def gauss_jordan(mat_in):
    '''
    Do Gauss-Jordan Matrix Inversion.
    A: n x n matrix in a list of lists.
    Return: Aaug, Ainv
        Aaug is the final augmented matrix.
        if the front part of Aaug appears to be identity,
        Ainv is a valid matrix inversion of A.
    '''
    # Get dimension
    n = len(mat_in)

    # Copy a matrix
    A = []
    for i in range(n):
        A.append(mat_in[i].copy())

    # Make an identity matrix I
    Imat = [[1*(i == j) for j in range(n)] for i in range(n)]

    # Augment A with I
    for i in range(n):
        A[i].extend(Imat[i])

    # Get the front part of A' to identity
    for i in range(n):
        # Make a diagonal element 1
        anchor = A[i][i]
        for j in range(i, 2 * n):
            A[i][j] /= anchor

        # Make an off-diagonal 0
        for k in range(n):
            if k != i:
                target = A[k][i]
                for j in range(2 * n):
                    if target != 0:
                        A[k][j] = A[k][j] - A[i][j] * target

    Ainv = []
    for i in range(n):
        Ainv.append(A[i][n:])

    return A, Ainv

if __name__ == '__main__':
    M0 = [[4, 2, 8], [3, 0, 9], [7, 5, 6]]
    print('A');     print(M0)

    M1, M2 = gauss_jordan(M0)

    print('Inverse of A');     print(M2)
