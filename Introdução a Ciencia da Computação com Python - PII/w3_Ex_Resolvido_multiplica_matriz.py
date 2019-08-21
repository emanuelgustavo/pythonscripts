import w3_Ex_Resolvido_cria_matriz as matriz

def multiplica_matriz(A, B):

    if len(A) == len(B[0]):
        
        num_lin = len(A)
        num_col = len(B[0])
        C = matriz.cria_matriz(num_lin, num_col, 0)

        for i in range(num_lin):
            for j in range(num_col):                
                resultado = 0
                for z in range(num_col):
                    resultado += A[i][z] * B[z][j]
                C[i][j] = resultado
        return C
        
    else:
        return False

if __name__ == '__main__':
    A = [[1,2],[3,4]]
    B = [[1,2],[3,4]]
    print(multiplica_matriz(A, B))
