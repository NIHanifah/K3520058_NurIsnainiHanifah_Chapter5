
#Ketentuan gaji awal
gajiA = 10000000
gajiB = 8500000
gajiC = 7000000
gajiD = 5500000

#potongan gaji
potonganA = gajiA - (gajiA*(2.5/100))
potonganB = gajiB - (gajiB*(2.0/100))
potonganC = gajiC - (gajiC*(1.5/100))
potonganD = gajiD - (gajiD*(1.0/100))

#Persen potongan gaji
golonganA = 2.5
golonganB = 2.0
golonganC = 1.5
golonganD = 1.0
#Golongan
golongan1 = 'A'
golongan2 = 'B'
golongan3 = 'C'
golongan4 = 'D'

#Tunjangan Istri atau Suamai
tunjanganIstriSuamiA = gajiA - (gajiA*(10/100))
tunjanganIstriSuamiB = gajiB - (gajiB*(10/100))
tunjanganIstriSuamiC = gajiC - (gajiC*(10/100))
tunjanganIstriSuamiD = gajiD - (gajiD*(10/100))

#Gaji kotor
gajiKotorA = gajiA + tunjanganIstriSuamiA
gajiKotorB = gajiB + tunjanganIstriSuamiB
gajiKotorC = gajiC + tunjanganIstriSuamiC
gajiKotorD = gajiD + tunjanganIstriSuamiD

#Gaji bersih
gajiBersihA = gajiKotorA - potonganA
gajiBersihB = gajiKotorB - potonganB
gajiBersihC = gajiKotorC - potonganC
gajiBersihD = gajiKotorD - potonganD

print("----AWALI KATA DENGAN HURUF KAPITAL----")

#!!!GUNAKAN HURUF KAPITAL SAAT INPUT GOLONGAN!!!
#!!!GUNAKAN HURUF KECIL SAAT INPUT STATUS MENIKAH!!!
#input data
kodeKaryawan = input("Masukkan kode karyawan          : ")
namaKaryawan = str(input("Masukkan nama karyawan          : "))
golongan = input("Masukkan golongan               : ")
statusMenikah = input("Masukkan status (Menikah/Belum) : ")

status1 = 'menikah'
status2 = 'Menikah'

#Kondisi jika sudah menikah
if statusMenikah == status1 or statusMenikah == status2:

    jumlahAnak = int(input("Masukkan jumlah anak            : "))

    #Output bagian judul
    print ("============================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("----------------------------")

    #Output bagian data pertama
    print("Nama Karyawan                   :", namaKaryawan, "(Kode: ", kodeKaryawan, ")")
    print("Golongan                        :", golongan)
    print("Status Menikah                  :", statusMenikah)
    print("Jumlah Anak                     :", jumlahAnak)
       
    #Tunjangan anak
    tunjanganAnakA = jumlahAnak * (gajiA - (gajiA*(5/100)))
    tunjanganAnakB = jumlahAnak * (gajiB - (gajiB*(5/100)))
    tunjanganAnakC = jumlahAnak * (gajiC - (gajiC*(5/100)))
    tunjanganAnakD = jumlahAnak * (gajiD - (gajiD*(5/100)))

    gajiKotorA = gajiA + tunjanganIstriSuamiA + tunjanganAnakA
    gajiKotorB = gajiB + tunjanganIstriSuamiB + tunjanganAnakB
    gajiKotorC = gajiC + tunjanganIstriSuamiC + tunjanganAnakC
    gajiKotorD = gajiD + tunjanganIstriSuamiD + tunjanganAnakD

        #Output bagian data kedua
    if golongan == golongan1:
        print("Gaji Pokok                      : Rp", gajiA)
        print("Tunjangan Istri/Suami           : Rp", int(tunjanganIstriSuamiA))
        print("Tunjangan Anak                  : Rp", int(tunjanganAnakA))
    elif golongan == golongan2:
        print("Gaji Pokok                      : Rp", gajiB)
        print("Tunjangan Istri/Suami           : Rp", int(tunjanganIstriSuamiB))
        print("Tunjangan Anak                  : Rp", int(tunjanganAnakB))
    elif golongan == golongan3:
        print("Gaji Pokok                      : Rp", gajiC)
        print("Tunjangan Istri/Suami           : Rp", int(tunjanganIstriSuamiC))
        print("Tunjangan Anak                  : Rp", int(tunjanganAnakC))
    elif golongan == golongan4:
        print("Gaji Pokok                      : Rp", gajiD)
        print("Tunjangan Istri/Suami           : Rp", int(tunjanganIstriSuamiC))
        print("Tunjangan Anak                  : Rp", int(tunjanganAnakD))
    else:
        print ("Nilai tidak valid")

    print ("-----------------------------")

        #Output bagian data ketiga
    if golongan == golongan1:
        print("Gaji Kotor                      : Rp", int(gajiKotorA))
        print("Potongan (", golonganA, "%)               : Rp", int(potonganA))
    elif golongan == golongan2:
        print("Gaji Kotor                      : Rp", int(gajiKotorB))
        print("Potongan (", golonganB, "%)               : Rp", int(potonganB))
    elif golongan == golongan3:
        print("Gaji Kotor                      : Rp", int(gajiKotorC))
        print("Potongan (", golonganC, "%)               : Rp", int(potonganC))
    elif golongan == golongan4:
        print("Gaji Kotor                      : Rp", int(gajiKotorD))
        print("Potongan (", golonganD, "% )              : Rp", int(potonganD))
    else:
        print ("Nilai tidak valid")

    print("---------------------------")

    #Output bagian akhir
    if golongan == golongan1:
        print("Gaji Akhir                      : Rp", int(gajiKotorA - potonganA))
    elif golongan == golongan2:
        print("Gaji Akhir                      : Rp", int(gajiKotorB - potonganB))
    elif golongan == golongan3:
        print("Gaji Akhir                      : Rp", int(gajiKotorC - potonganC))
    elif golongan == golongan4:
        print("Gaji Akhir                      : Rp", int(gajiKotorD - potonganD))
    else:
            print ("Nilai tidak valid")

#Kondisi jika belum menikah
else:

    print ("-----------------------------")

    #Output bagian data kedua
    if golongan == golongan1:
        print("Gaji Pokok                      :Rp ", gajiA)
    elif golongan == golongan2:
        print("Gaji Pokok =                    :Rp ", gajiB)
    elif golongan == golongan3:
        print("Gaji Pokok =                    :Rp ", gajiC)
    elif golongan == golongan4:
        print("Gaji Pokok                      :Rp ", gajiD)
    else:
        print ("Nilai tidak valid")


    print ("-----------------------------")

    #Output bagian data ketiga
    if golongan == golongan1:
        print("Gaji Kotor                      : Rp", int(gajiKotorA))
        print("Potongan (", golonganA, "%)               : Rp", int(potonganA))
    elif golongan == golongan2:
        print("Gaji Kotor                      : Rp", int(gajiKotorB))
        print("Potongan (", golonganB, "%)               : Rp", int(potonganB))
    elif golongan == golongan3:
        print("Gaji Kotor                      : Rp", int(gajiKotorC))
        print("Potongan (", golonganC, "%)               : Rp", int(potonganC))
    elif golongan == golongan4:
        print("Gaji Kotor                      : Rp", int(gajiKotorD))
        print("Potongan (", golonganD, "% )              : Rp", int(potonganD))
    else:
        print ("Nilai tidak valid")

    print("---------------------------")

    #Output bagian akhir
    if golongan == golongan1:
        print("Gaji Akhir                      : Rp", int(gajiKotorA - potonganA))
    elif golongan == golongan2:
        print("Gaji Akhir                      : Rp", int(gajiKotorB - potonganB))
    elif golongan == golongan3:
        print("Gaji Akhir                      : Rp", int(gajiKotorC - potonganC))
    elif golongan == golongan4:
        print("Gaji Akhir                     : Rp", int(gajiKotorD - potonganD))
    else:
        print ("Nilai tidak valid")