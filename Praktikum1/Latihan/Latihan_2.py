range (0,101)

#Input nilai
a = float(input("Masukkan nilai Bahasa Indonesia : "))
b = float(input("Masukkan nilai IPA              : "))
c = float(input("Masukkan nilai Matemaika        : "))

#Kondisi nilai tidak memenuhi range
if a not in range (0,101):
    print ("Maaf input nilai Bahasa Indonesia tidak valid") 

if b not in range (0,101):
    print ("Maaf input nilai IPA tidak valid")

if c not in range (0,101):
    print ("Maaf input nilai Matematika tidak valid") 

#Kondisi pernyataan lulus atau tidak lulus
if a not in range (0,101) or b not in range (0,101) or c not in range (0,101):
    breakpoint
elif (a > 60) and (b > 60) and (c>70):
    print ("Status Kelulusan                : Lulus")
else:
    print ("Status Kelulusan                : Tidak Lulus")

