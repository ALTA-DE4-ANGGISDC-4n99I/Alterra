def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b
def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a // b  
def main():
    penjumlahan_input = (3, 4)
    pengurangan_input = (15, 4)
    perkalian_input = (10, 10)
    pembagian_input = (12, 3)

    penjumlahan_output = penjumlahan(*penjumlahan_input)
    pengurangan_output = pengurangan(*pengurangan_input)
    perkalian_output = perkalian(*perkalian_input)
    pembagian_output = pembagian(*pembagian_input)
    
    print("Penjumlahan:", penjumlahan_output)
    print("Pengurangan:", pengurangan_output)
    print("Perkalian:", perkalian_output)
    print("Pembagian:", pembagian_output)
main()
