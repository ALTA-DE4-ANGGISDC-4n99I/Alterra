def check_number(n):
    if 0 <= n <= 34:
        return "D"
    elif 35 <= n <= 49:
        return "C"
    elif 50 <= n <= 64:
        return "B"
    elif 65 <= n <= 79:
        return "B+"
    elif 80 <= n <= 100:
        return "A"
    else:
        return "Nilai Tidak Valid."

n = int(input("Input Nilai : "))
print("")
print(check_number(n))
