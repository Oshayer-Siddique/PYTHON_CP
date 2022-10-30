import numpy as np
A = np.array([[1,0]])
B = np.array([[0,1]])
C = (A+B)/np.sqrt(2)
D = (A-B)/np.sqrt(2)
print(C)
print(D)


A = np.array([[1,1j]])/np.sqrt(2)
B = A.conj().T
print(A)
print(B)


Z = np.array([[1,0],[0,-1]])
H = np.array([[1,1],[1,-1]])/np.sqrt(2)
psi = np.array([[0],[1]])
print (H @ Z@ psi)