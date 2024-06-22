def cetak_table_perkalian(N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print("{:3}".format(i * j), end=" ")
        print()

if __name__ == '__main__':
    N = int(input("Masukkan nilai : "))
    print("Output:")
    cetak_table_perkalian(N)
