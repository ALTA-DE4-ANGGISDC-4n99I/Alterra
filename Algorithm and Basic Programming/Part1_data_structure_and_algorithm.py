# #problem 1 Remove duolicates

# def remove_duplicates(array):
#     unique_elements = []
#     for element in array:
#         if element not in unique_elements:
#             unique_elements.append(element)
#     return len(unique_elements)

# if __name__ == '__main__':
#     # Contoh penggunaan fungsi remove_duplicates
#     arr1 = [2, 3, 3, 3, 6, 9, 9]
#     arr2 = [2, 3, 4, 5, 6, 9, 9]
#     arr3 = [2, 2, 2, 11]
#     arr4 = [1, 2, 3, 11, 11]

#     print(f"Jumlah elemen unik di arr1: {remove_duplicates(arr1)}")  # 4
#     print(f"Jumlah elemen unik di arr2: {remove_duplicates(arr2)}")  # 6
#     print(f"Jumlah elemen unik di arr3: {remove_duplicates(arr3)}")  # 2
#     print(f"Jumlah elemen unik di arr4: {remove_duplicates(arr4)}")  # 4

#part 2 prima ke X

# def primeX(n):
#     def is_prime(num):
#         if num <= 1:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     count = 0
#     num = 2
#     while True:
#         if is_prime(num):
#             count += 1
#             if count == n:
#                 return num
#         num += 1

# print(primeX(1)) 
# print(primeX(4))  
# print(primeX(6))  
# print(primeX(10)) 

#part 3 fibonacci

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# fibonacci(10) 

#part 4 prima segi 4

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_grid(width, height, start):
    result = ""
    primes = []
    num = start + 1
    
    # Mengumpulkan bilangan prima yang dibutuhkan
    while len(primes) < width * height:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    # Membentuk grid dalam bentuk string
    for i in range(height):
        row = primes[i * width:(i + 1) * width]
        result += ' '.join(map(str, row)) + "\n"
    
    return result

# Contoh penggunaan
print(generate_primes_grid(2, 3, 13))
print(generate_primes_grid(5, 2, 1))



