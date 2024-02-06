import numpy as np
#problem 1
e = np.array([1, 2, 3, 4])
print(e)
print()
z = np.zeros((4, 3))
print(z)
print()
o = np.ones((3,4))
print(o)
print()

#problem 2
A = np.array([(3, 5, 9), (4, 7, 8)])
B = np.array([(4, 5, 6, 1), (7, 8, 9, 10), (11, 12, 13, 14)])
print(A)
print()
print(B)
print()
C = A @ B
print(C)
print()

#problem 3
array = np.array([(3,1), (1,2)])
eigen = np.linalg.eig(array)
print(eigen)

