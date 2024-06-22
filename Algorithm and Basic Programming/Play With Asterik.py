def play_with_asterik(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

if __name__ == '__main__':
    rows = int(input("Masukkan Nilai: "))
    play_with_asterik(rows)
