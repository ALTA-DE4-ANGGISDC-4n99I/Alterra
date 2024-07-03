def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(a, b, c):
    return a + b + c
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def main():
    luas_persegi_input = 4
    luas_segitiga_input = (3, 4)
    luas_persegi_panjang_input = (7, 8)
    
    keliling_persegi_input = 4
    keliling_segitiga_input = (3, 4, 5)
    keliling_persegi_panjang_input = (7, 8)

    luas_persegi_output = luas_persegi(luas_persegi_input)
    luas_segitiga_output = luas_segitiga(*luas_segitiga_input)
    luas_persegi_panjang_output = luas_persegi_panjang(*luas_persegi_panjang_input)

    keliling_persegi_output = keliling_persegi(keliling_persegi_input)
    keliling_segitiga_output = keliling_segitiga(*keliling_segitiga_input)
    keliling_persegi_panjang_output = keliling_persegi_panjang(*keliling_persegi_panjang_input)
    
    print("Luas")
    print(f"Persegi: {luas_persegi_output}")
    print(f"Segitiga: {luas_segitiga_output}")
    print(f"Persegi Panjang: {luas_persegi_panjang_output}")
    
    print("\nKeliling")
    print(f"Persegi: {keliling_persegi_output}")
    print(f"Segitiga: {keliling_segitiga_output}")
    print(f"Persegi Panjang: {keliling_persegi_panjang_output}")
main()
