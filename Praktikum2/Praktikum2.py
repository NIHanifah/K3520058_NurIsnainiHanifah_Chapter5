#Nomor 2
print("----Nomor 2----")
i = 0
while (i < 10):
    print('Hello World')
    i += 1

#Nomor 4
print("----Nomor 4----")
n = int(input("Banyaknya perulangan = "))
i = 0
while (i < n):
    print('Hello World')
    i += 1

#Nomor 5
print("----Nomor 5----")
i = 2
while (i <= 20):
    print('Hello World')
    i += 2

#Nomor 6
print("----Nomor 6----")
i = 0
while True:
    print('Hello World')
    i += 1
    if (i == 6):
        break

#Nomor 7
print("----Nomor 7----")
perulangan = int(input("Banyaknay perulangan = "))
i = 0
while True:
    print('Hello World')
    i += 1
    if (i == perulangan):
        break

#Nomor 8
print("----Nomor 8----")
print("Membuat bintang ajaib")
kolom = 5
baris = 5

i = 0
while (i < baris):
    j = 0
    while (j < kolom):
        print('*', end='')
        j += 1
    print(' ')
    i += 1

#Nomor 10
print("----Nomor 11----")
n = 1
x = 5

# Mengulang Baris
while n <= x:
	kol = n

	# Mengulang Kolom
	while kol > 0:
		print("*", end=" ")
		kol -= 1
	print()
	n += 1

#Nomor 11
print("----Nomor 11----")
from random import randint
while True:
    bil = randint(0, 10)
    print(bil)
    if bil == 5:
        break

#Nomor 13
print("----Nomor 14----")
from random import randint
j = 0
while True:
    bil = randint(0, 10)
    print(bil)
    j += 1
    if bil == 5:
        break
print("Jumlah Perulangan =", j)