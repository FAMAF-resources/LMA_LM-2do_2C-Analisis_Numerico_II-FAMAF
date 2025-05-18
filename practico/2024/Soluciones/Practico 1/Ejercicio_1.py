import numpy as np 

# Primera parte C = AB
 
A_11 = np.array([[1.], [2]])

A_12 = np.array([[3.,2], [1,1]])

A_21 = np.array([[-1.]])

A_22 = np.array([0., 1])

A = np.block([[A_11, A_12], [A_21, A_22]])

# print(f'A ={A}')

B_11 = np.array([[1.]])

B_12 = np.array([[0.,1]])

B_21 = np.array([[2.], [-1]])

B_22 = np.array([[1., 1], [2, 0]])

B = np.block([[B_11, B_12], [B_21, B_22]])

# print(f'B ={B}')

C = A@B

# print(f'C ={C}')

# Segunda parte C_ij = A_i1@B_1j + A_i2@B_2j con i,j = 1,2

# Casos para filas 
# A[:, j] Corre todas las filas de la columna numero j
# A[i:, j] Corre desde la fila numero i hasta el ultima fila de la columna numero j
# A[:i, j] Corre desde la primera fila hasta la fila numero i-1 de la columna 
# numero j
# A[i:k, j] Corre desde la fila i hasta la fila k-1 de la columna j 

# Casos de columnas
# A[i, :] Corre todas las columnas de la fila i
# A[i, j:] Corre desde la columna numero j hasta el ultimo elemento de la fila 
# numero i
# A[i, :j] Corre desde la primera columna hasta la columna numero j-1 de la fila 
# numero j
# A[i, j:k] Corre desde la columna j hasta la columna k-1 de la fila i 

# Casos comvinados
# A[i:k, j:l] Corre desde la fila i a la fila k-1 y corre desde 
# la columna j hasta la columna l-1. 

A_11 = A[0:2, 0]
A_12 = A[0:2, 1:3]
A_21 = A[2,0]
A_22 = A[2, 1:3]

B_11 = B[0, 0]
B_12 = B[0,1:3]
B_21 = B[1:3,0]
B_22 = B[1:3,1:3]

C_11 = A_11*B_11 + A_12 @ B_21

C_12 = np.outer(A_11,B_12) + A_12@B_22

C_21 = A_21*B_11 + A_22@B_21

C_22 = A_21*B_12 + A_22@B_22

print(f'C_11 = {C_11}')
print(f'C_12 = {C_12}')
print(f'C_21 = {C_21}')
print(f'C_22 = {C_22}')












