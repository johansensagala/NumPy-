import numpy as np

vektor1 = np.array([4, 5, 6, 7])
vektor2 = np.array([8, 4, 2, 2])
vektor3 = np.array([6, 3, 1, 10])
matriks1 = np.array([[1, 2],[3, 4]])
matriks2 = np.array([[3, 4],[2, 6]])
matriks3 = np.array([[5, 6],[2, 7],[5, 8]])
matriks4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

# penjumlahan elemen vektor dengan angka yang sama
vektor4 = vektor1 + 8

print(vektor4)

# penjumlahan dua vektor / matriks
vektor5 = vektor1 + vektor2
vektor5_2 = np.add(vektor1, vektor2)

print(vektor5)
print(vektor5_2)

# pengurangan dua vektor / matriks
vektor6 = vektor3 - vektor2
vektor6_2 = np.subtract(vektor3, vektor2)

print(vektor6)
print(vektor6_2)

# perkalian matriks

matriks_kali = matriks1 * matriks2 # bukan perkalian dot matriks
matriks_kali2 = np.matmul(matriks1, matriks2)
matriks_kali3 = matriks1.dot(matriks2)

print(matriks_kali)
print(matriks_kali2)
print(matriks_kali3)

# perpangkatan patriks

matriks_kuadrat = matriks4**2

print(matriks_kuadrat)

# akar matriks

akar_matriks = np.sqrt(matriks4)

print(akar_matriks)

# transpose matriks

matriks_transpose = np.transpose(matriks3)

print(matriks_transpose)