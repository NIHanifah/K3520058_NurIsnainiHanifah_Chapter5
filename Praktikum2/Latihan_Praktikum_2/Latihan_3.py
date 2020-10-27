#Mendefinisikan variabel
n = 0 
j = 0
hitung = 0

#Melakukan perulangan
while(n < 100 ):
    n += 1
    if n % 2 == 1:
        print (n)
        j += 1
        hitung += n

print("Banyaknya bilangan ganjil : ", j)
print ("Jumlah seluruh bilangan : ", int(hitung))