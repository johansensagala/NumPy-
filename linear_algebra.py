import numpy as np

matriks1 = np.array([[1, 4],[3, 4]])
matriks2 = np.array([[2, 5],[4, 8],[9, 7]])
matriks3 = np.array([[1, 2, 3],[4, 8, 6],[7, 8, 9]])

# invers_matriks

invers_matriks1 = np.linalg.inv(matriks1)
invers_matriks3 = np.linalg.inv(matriks3)

print(invers_matriks1)
print(invers_matriks3)

# determinan matriks

determinan_matriks1 = np.linalg.det(matriks1)
determinan_matriks3 = np.linalg.det(matriks3)

print(determinan_matriks1)
print(determinan_matriks3)

# persamaan linear

# 2x + 3y = 23
# 5x - y = 15

koefisien = np.array([[2, 3],[5, -1]])
hasil = np.array([23, 15])

solusi = np.linalg.solve(koefisien, hasil)

print(solusi)

# x + 7y + 3z = 44
# 2x + 2y + z = 17
# 3x + 8y + 10z = 100

koefisien2 = np.array([[1, 7, 3],[2, 2, 1],[3, 8, 10]])
hasil2 = np.array([44, 17, 100])

solusi2 = np.linalg.solve(koefisien2, hasil2)

print(solusi2)

# matriks eigen

matriks_eigen = np.linalg.eig(matriks3)

print(matriks_eigen)

# dekomposisi LU

a = np.array([[1, 5, 3],[1, -2, 9],[2, 1, -1]])

matriks_qr = np.linalg.qr(a)

print(matriks_qr)