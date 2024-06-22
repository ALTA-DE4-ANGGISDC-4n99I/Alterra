def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Masukkan teks: ")
if palindrome(input_string):
    print("String tersebut adalah palindrome.")
else:
    print("String tersebut bukan palindrome.")
