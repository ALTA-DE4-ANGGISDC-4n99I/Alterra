def pangkat(base, exponent):
    return base ** exponent

base_value = float(input("Masukkan nilai: "))
exponent_value = float(input("Masukkan nilai eksponen: "))

result = pangkat(base_value, exponent_value)
print(f"{base_value} pangkat {exponent_value} = {result}")
