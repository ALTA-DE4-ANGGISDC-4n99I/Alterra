def ubah_huruf(text):
    shifted_alphabet = 'KLMNOPQRSTUVWXYZABCDEFGHIJ'
    ubah_text = []

    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted_char = shifted_alphabet[ord(char) - ord('A')]
            else:
                shifted_char = shifted_alphabet[ord(char) - ord('a')]
            ubah_text.append(shifted_char)
        else:
            ubah_text.append(char)

    return ''.join(ubah_text)

if __name__ == '__main__':
    plaintext = input("Masukkan teks : ")
    ubah_text = ubah_huruf(plaintext)
    print("Output:", ubah_text)
