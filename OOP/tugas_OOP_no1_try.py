def fun_luas_persegi(sisi):
    return sisi * sisi
def fun_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

print("---------- Hitung Luas ----------")

luas_persegi = int(input("Persegi : "))
print("")
alas_segitiga = int(input("Alas Segitiga : "))
print("")
tinggi_segitiga = int(input("Tinggi Segitiga : "))
print("")
luas_persegi_panjang = int(input("Persegi Panjang : "))
print("")

print("---------- Hitung Keliling ----------")
keliling_persegi = int(input("Persegi : "))
print("")
keliling_segitiga = int(input("Segitiga : "))
print("")
keliling_persegi_panjang = int(input("Persegi Panjang : "))
print("")

output_luas_persegi = fun_luas_persegi(luas_persegi)
output_luas_segitiga = fun_luas_segitiga(alas_segitiga, tinggi_segitiga)

print(f"Luas Persegi Adalah : {output_luas_persegi}")
print(f"Luas Segitiga Adalah : {output_luas_segitiga}")
