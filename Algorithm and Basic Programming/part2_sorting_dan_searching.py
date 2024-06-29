#problem 1 find min and max number
# def find_min_and_max(arr):
#     min_val = float('inf')
#     max_val = float('-inf')
#     min_index = None
#     max_index = None

#     for i, num in enumerate(arr):
#         if num < min_val:
#             min_val = num
#             min_index = i
#         if num > max_val:
#             max_val = num
#             max_index = i

#     return f"min: {min_val} index: {min_index} max: {max_val} index: {max_index}"

# print(find_min_and_max([5, 7, 4, -2, -1, 8]))
# print(find_min_and_max([2, -5, -4, 22, 7]))
# print(find_min_and_max([-1,5,6,4,2,18]))
# print(find_min_and_max([-2,5,-7,4,7,-20]))

#problem 2 maximum buy product

# def maximum_buy_product(money, product_price):
#     sorted_prices = sorted(product_price, reverse=True)
#     total_products = 0

#     for price in sorted_prices:
#         if money >= price:
#             money -= price
#             total_products += 1
#         else:
#             break

#     return total_products

# # Contoh penggunaan
# print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))  # Output: 3
# print(maximum_buy_product(30000, [15000, 10000, 12000, 5000]))  # Output: 4
# print(maximum_buy_product(10000, [2000, 3000, 2500]))  # Output: 4
# print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))
# print(maximum_buy_product(0, [10000, 30000]))  # Output: 0

#problem 3 playing domino

# def playing_domino(cards, deck):
#     valid_cards = []
#     for card in deck:
#         if card in cards:
#             valid_cards.append(card)
#     return valid_cards

# print(playing_domino([[6, 5], [3, 4]], [[2, 1], [3, 3], [1, 4]]))

# print(playing_domino([[6, 5], [3, 4]], [[2, 1], [2, 3], [1, 4]]))

# print(playing_domino([[6, 5], [3, 4]], [[2, 1], [2, 3], [1]]))

#part 4 count item and sort

def count_item_and_sort(items):
    item_count = {}
    for item in items:
        item_count[item] = item_count.get(item, 0) + 1

    result = ""
    for item, count in sorted(item_count.items(), key=lambda x: (-x[1], x[0])):
        result += f"{item}->{count} "

    return result.strip()

print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "D", "D"]))
print(count_item_and_sort(["football", "basketball", "tenis"]))




