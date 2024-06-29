#Problem 1 - Bilangan Prima
def prime_number(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

print(prime_number(1000000007))  
print(prime_number(1500450271))  
print(prime_number(1000000000))  
print(prime_number(10000000019)) 
print(prime_number(10000000033)) 


#problem 2 fast exponentiation
def pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / pow(x, -n)
    elif n % 2 == 0:
        half_pow = pow(x, n // 2)
        return half_pow * half_pow
    else:
        return x * pow(x, n - 1)

print(pow(2, 3))  
print(pow(7, 2))  
print(pow(10, 5))  
print(pow(17, 6))  
print(pow(5, 3))  

#Problem 3 - Join Array Remove Duplicate
def join_array_remove_duplicate(arrayA, arrayB):
    combined_set = set(arrayA).union(set(arrayB))
    return list(combined_set)

print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))

#Problem 4 - Angka Muncul Sekali
def muncul_sekali(angka):
    frekuensi = {}
    
    for char in angka:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1
    
    hasil = [int(char) for char in frekuensi if frekuensi[char] == 1]
    
    return hasil


print(muncul_sekali("1234123")) 
print(muncul_sekali("76523752")) 
print(muncul_sekali("12345")) 
print(muncul_sekali("1122334455"))
print(muncul_sekali("0872504")) 

#problem 5 Pair with Target Sum

def pair_sum(arr, target):
    left, right = 0, arr.length - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Test cases
print(pair_sum([1, 2, 3, 4, 6], 6))
print(pair_sum([2, 5, 9, 11], 11)) 
print(pair_sum([1, 3, 5, 7], 12)) 
print(pair_sum([1, 4, 6, 8], 10)) 
print(pair_sum([1, 5, 6, 7], 6)) 


