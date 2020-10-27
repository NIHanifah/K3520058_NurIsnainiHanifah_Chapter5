range (0,100)

#Input nilai
a = float(input("Masukkan nilai Bahasa Indonesia : "))
b = float(input("Masukkan nilai IPA              : "))
c = float(input("Masukkan nilai Matemaika        : "))

#Kondisi pernyataan lulus atau tidak lulus
if (a > 60) and (b > 60) and (c>70):
    print ("Status Kelulusan                : Lulus")
else:
    print ("Status Kelulusan                : Tidak Lulus")


    