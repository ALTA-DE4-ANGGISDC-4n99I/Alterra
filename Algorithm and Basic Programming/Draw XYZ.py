def draw_xyz(N):
    count = 1
    for i in range(N):
        for j in range(N):
            if count % 3 == 0:
                print('X', end=' ')
            elif count % 2 == 1:
                print('Y', end=' ')
            else:
                print('Z', end=' ')
            count += 1
        print()

if __name__ == '__main__':
    N = int(input("Masukkan nilai : "))
    draw_xyz(N)
