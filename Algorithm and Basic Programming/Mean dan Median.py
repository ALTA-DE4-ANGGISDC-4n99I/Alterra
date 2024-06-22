def mean_median(array_input):
    total = sum(array_input)
    mean = total / len(array_input)
    rounded_mean = round(mean, 1)

    n = len(array_input)
    if n % 2 == 1:
        median = array_input[(n - 1) // 2]
    else:
        mid1 = array_input[n // 2 - 1]
        mid2 = array_input[n // 2]
        median = (mid1 + mid2) / 2
    
    return rounded_mean, median

def process_input(input_str):
    input_str = input_str.strip()[1:-1]
    array_input = list(map(int, input_str.split(',')))
    result = mean_median(array_input)
    return result

if __name__ == '__main__':
    input_str = input("Masukkan array angka dalam format [1, 2, 3, 4]: ")
    result = process_input(input_str)
    print(f"Output: {result[0]} {result[1]}")
