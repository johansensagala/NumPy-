import numpy as np

# membuat vektor
vektor1 = np.array([1, 2, 3, 4])
vektor2 = np.array([3, 2, 5, 4])
vektor3 = np.array([1, 6, 3, 8])

# membuat matriks
matriks = np.array([[1, 2],[3, 4],[5, 6]])

print(matriks)

# membuat matriks dari vektor
matriks2 = np.array([vektor1, vektor2, vektor3])

print(matriks2)

# membuat matriks identitas
matriks_identitas = np.eye(3, dtype=int)
matriks_identitas2 = np.identity(4, dtype=int)

print(matriks_identitas)
print(matriks_identitas2)

# membuat matriks yang semua elemennya sama
matriks_nol = np.zeros((3, 3))
matriks_satu = np.ones((3, 4))

print(matriks_nol)
print(matriks_satu)

# menyusun matriks / vektor
vektor_aritmatika = np.arange(0, 10)
vektor_aritmatika2 = np.arange(1, 20, 2.5)

print(vektor_aritmatika)
print(vektor_aritmatika2)

# menambah elemen array
vektor4 = np.append(vektor1, [5, 6])
vektor5 = np.concatenate((vektor2, np.arange(8, 12)))
vektor6 = np.insert(vektor3, 0, vektor2)

print(vektor4)
print(vektor5)
print(vektor6)