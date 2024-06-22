def full_prima(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_full_prima(n):
    if not full_prima(n):
        return False
    str_n = str(n)
    for digit_char in str_n:
        digit = int(digit_char)
        if not full_prima(digit):
            return False
    return True

if __name__ == '__main__':
    n = int(input("Input: "))
    if is_full_prima(n):
        print("Output: true")
    else:
        print("Output: false")
