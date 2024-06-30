def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# Fungsi untuk menghitung volume tabung
def volume_tabung(jari_jari, tinggi):
    return math.pi * (jari_jari ** 2) * tinggi

# Fungsi utama untuk mengatur input dan output
def main():
    # Input
    volume_kubus_input = 10
    volume_balok_input = (3, 6, 10)
    volume_tabung_input = (7, 10)
    
    # Menghitung volume
    volume_kubus_output = volume_kubus(volume_kubus_input)
    volume_balok_output = volume_balok(*volume_balok_input)
    volume_tabung_output = volume_tabung(*volume_tabung_input)
    
    # Output
    print("Volume")
    print(f"Kubus: {volume_kubus_output}")
    print(f"Balok: {volume_balok_output}")
    print(f"Tabung: {volume_tabung_output}")