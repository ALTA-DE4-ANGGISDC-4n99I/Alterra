def calculate_shipping_cost(length, width, height, weight):
    # Hitung volume
    volume = length * width * height
    
    # Periksa apakah volume kurang dari ukuran minimal (50 cm^3)
    if volume < 50:
        volume = 50
    
    # Periksa apakah berat kurang dari berat minimal (1 kg)
    if weight < 1:
        weight = 1
    
    # Hitung harga berdasarkan tarif standar Rp. 5000 per kg atau bagian dari kg.
    harga = max(volume // 50, weight) * 5000
    
    return harga

# Contoh penggunaan
panjang_input = 5
lebar_input = 2
tinggi_input = 4
berat_input = 1

# Panggil fungsi dan cetak harga yang dihitung
harga_output = calculate_shipping_cost(panjang_input, lebar_input, tinggi_input, berat_input)
print(f"Harga: Rp{harga_output}")
