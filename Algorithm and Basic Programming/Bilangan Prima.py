def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

bilangan = int(input("Masukkan bilangan: "))
if prime_number(bilangan):
    print(bilangan, "adalah bilangan prima.")
else:
    print(bilangan, "bukan bilangan prima.")
