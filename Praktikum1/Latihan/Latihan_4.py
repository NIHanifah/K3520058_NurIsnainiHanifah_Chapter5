
#Ketentuan gaji awal
gajiA = 10000000
gajiB = 8500000
gajiC = 7000000
gajiD = 5500000

#Gaji setelah potongan
gajiAkhirA = gajiA - (gajiA*(2.5/100))
gajiAkhirB = gajiB - (gajiB*(2.0/100))
gajiAkhirC = gajiC - (gajiC*(1.5/100))
gajiAkhirD = gajiD - (gajiD*(1.0/100))

#Golongan
golongan1 = 'A'
golongan2 = 'B'
golongan3 = 'C'
golongan4 = 'D'

print('----AWALI KATA DENGAN HURUF KAPITAL----')

kodeKaryawan = int(input("Masukkan kode karyawan : "))
namaKaryawan = str(input("Masukkan nama karyawan : "))
golongan = input("Masukkan golongan      : ")

print ("============================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("----------------------------")

print("Nama Karyawan          : ", namaKaryawan, "(Kode: ", kodeKaryawan, ")")
print("Golongan               : ", golongan)

print ("-----------------------------")

if golongan == golongan1:
    print("Gaji Pokok             :Rp ", gajiA)
    print("Potongan               :Rp ", gajiAkhirA)
    print("Gaji Bersih            :Rp ", gajiA - gajiAkhirA)
elif golongan == golongan2:
    print("Gaji Pokok =           :Rp ", gajiB)
    print("Potongan               :Rp ", gajiAkhirB)
    print("Gaji Bersih            :Rp ", gajiB - gajiAkhirB)
elif golongan == golongan3:
    print("Gaji Pokok =           :Rp ", gajiC)
    print("Potongan               :Rp ", gajiAkhirC)
    print("Gaji Bersih            :Rp ", gajiC - gajiAkhirC)
elif golongan == golongan4:
    print("Gaji Pokok =           :Rp ", gajiD)
    print("Potongan               :Rp ", gajiAkhirD)
    print("Gaji Bersih            :Rp ", gajiD - gajiAkhirD)
else:
    print ("Nilai tidak valid")

