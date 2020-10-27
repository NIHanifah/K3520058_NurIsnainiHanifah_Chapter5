n = 5
i = 1

#Membuat perulangan bintang
while i <= n :
    j = n
    while j >= i:
        print("*", end = " ")
        j -= 1
    print()
    i += 1