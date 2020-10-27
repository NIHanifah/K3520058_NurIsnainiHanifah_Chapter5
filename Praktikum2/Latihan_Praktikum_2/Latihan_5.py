#Mengimport bilangan random
import random
n = random.randint(1, 100)

#Perulangan 
for angkaTebakan in range (0, 100):
    angkaTebakan = int(input("Tebakan Anda = "))
    if angkaTebakan < n:
        print ("Bilangan anda terlalu kecil")
    elif angkaTebakan > n:
        print ("Bilangan anda terlalu besar")
    elif angkaTebakan == n:
        print ("Selamat anda berhasil. Yeee")
        break
    