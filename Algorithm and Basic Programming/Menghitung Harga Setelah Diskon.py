Harga = int(input("Input Harga : "))
print("")

Diskon = int(input("Input Diskon : "))
print("")

Hasil_Potong_Diskon = (Diskon / 100) * Harga
Hasil_Akhir = Harga - Hasil_Potong_Diskon


print(Hasil_Akhir)