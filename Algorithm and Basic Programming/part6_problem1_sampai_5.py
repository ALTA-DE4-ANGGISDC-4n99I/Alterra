#problem 1 Compare String

def compare(a, b):
    
    max_substr = ""
    len_a, len_b = len(a), len(b)
    for i in range(len_a):
        for j in range(i + 1, len_a + 1):
            substr = a[i:j]
            if substr in b and len(substr) > len(max_substr):
                max_substr = substr
                
    return max_substr
print(compare("AKA", "AKASHI")) 
print(compare("KANGOORO", "KANG")) 
print(compare("KI", "KIJANG")) 
print(compare("KUPU-KUPU", "KUPU")) 
print(compare("ILALANG", "ILA")) 

#problem 2 caesar cipher
def caesar(offset, input_str):
    result = []
    for char in input_str:
        if char == ' ': 
            result.append(char)
        else:
            new_char = chr(((ord(char) - 97 + offset) % 26) + 97)
            result.append(new_char)
    return ''.join(result)

print(caesar(3, "abc")) 
print(caesar(2, "alta")) 
print(caesar(10, "alterraacademy")) 
print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) 
print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) 

#problem 3 Array Unique

def array_unique(arrayA, arrayB):
    
    setB = set(arrayB)
    result = []
    
    for num in arrayA:
        if num not in setB:
            result.append(num)
    
    return result

print(array_unique([1, 2, 3, 4], [1, 3, 5, 10, 16])) 
print(array_unique([10, 20, 30, 40], [5, 10, 15, 59]))  
print(array_unique([1, 3, 7], [1, 3, 5]))  
print(array_unique([3, 8], [2, 8])) 
print(array_unique([1, 2, 3], [3, 2, 1])) 

#Problem 4 - Maximum Sum Subarray of Size K

def find_max_sum_sub_array(k, arr):
    if len(arr) < k:
        return None
    max_sum = 0
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) 
print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) 
print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) 
print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) 
print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1]))

#Problem 5 - Remove Duplicates

def remove_duplicates(array):
    if not array:
        return 0
    next_non_duplicate = 1
    
    for i in range(1, len(array)):
        if array[next_non_duplicate - 1] != array[i]:
            array[next_non_duplicate] = array[i]
            next_non_duplicate += 1
    
    return next_non_duplicate

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) 
print(remove_duplicates([2, 2, 2, 11])) 
print(remove_duplicates([2, 2, 2, 11])) 
print(remove_duplicates([1, 2, 3, 11, 11])) 

