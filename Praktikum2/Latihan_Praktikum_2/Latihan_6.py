#Mengimport angka random
import random
n = random.randint(1, 100)
print("Halo, mari kita main tebak-tebakkan angka.")
print("Aku sudah memilih satu angka, silahkan kau menebaknya.")
#Data variabel
nilai = 100

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
    nilai -= 2
    if nilai == 0:
        print ("Game Over")
        break

print ("Score Anda: ", nilai)
