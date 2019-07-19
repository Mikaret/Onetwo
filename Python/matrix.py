import stdarray
import stdio
import sys


def main():
    M = int(sys.argv[1]) + 1
    N = int(sys.argv[2]) + 1
    mat = stdarray.create2D(M+1, N+1, 0)
    for i in range(M+1):
        mat[i][N] = 2*(M - 1)
    for j in range(N+1):
        mat[M][j] = 3*(N - j)

    g = min(M, N)
    for a in range(1, g):
        i = M-a
        j = N-a
        mat[i][j] = min(mat[i+1][j+1]+1, mat[i+1][j]+2, mat[i][j+1]+1)
        for m in range(i, -1, -1):
            mat[m][j] = min(mat[m+1][j+1] + 1, mat[m+1][j]+2, mat[m][j+1]+1)
        for m in range(j, -1, -1):
            mat[i][m] = min(mat[i+1][m+1] + 1, mat[i+1][m]+2, mat[i][m+1]+1)
    mat[0][0] = min(mat[1][1]+1, mat[1][0]+2, mat[0][1]+1)

    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            stdio.writef(' %3d\n', mat[i][j])
        elif (j == 0):
            stdio.writef(' %3d', mat[i][j])
        else:
            stdio.writef(' 3%d', mat[i][j])
    
if __name__ == "__main__":
    main()
