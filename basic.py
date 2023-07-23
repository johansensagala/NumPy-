import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list a = {list_a}")
print(f"vector a = {vector_a}")
print(f"vector a ^ 2 = {vector_a**2}")
print(f"vector a x 2 = {vector_a*5}")

matriks_b = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriks_c = np.array([[2,3,4],[5,6,7],[8,9,10]])

print(f"matriks b =\n{matriks_b}")
print(f"matriks b ^ 2 =\n{matriks_b**2}")

zeros_c = np.zeros((2,2))
print(f"matriks a =\n{zeros_c}")

ones_d = np.ones((3,2))
print(f"matriks d =\n{ones_d}")

# bukan perkalian matriks, namun hanya perkalian antara pasangan elemen
print(f"matriks b x matriks c =\n{matriks_b} x {matriks_c}\n {matriks_b*matriks_c}")

# perkalian matriks (perkalian dot)
print(f"matriks b x matriks c =\n{matriks_b} . {matriks_c}\n {np.dot(matriks_b,matriks_c)}")
