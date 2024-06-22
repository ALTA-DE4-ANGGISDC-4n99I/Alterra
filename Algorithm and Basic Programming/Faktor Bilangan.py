def print_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    num = int(input("Masukkan bilangan: "))
    result = print_factors(num)
    print("Faktor dari", num, "adalah:", ", ".join(map(str, result)))
