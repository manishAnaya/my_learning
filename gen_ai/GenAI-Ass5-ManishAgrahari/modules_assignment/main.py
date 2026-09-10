import math_utils
import string_utils
from math_utils import add, subtract
import shop_package.discount as disc
from shop_package import calculate_total, apply_tax

# Math Utils
print(add(10, 20))
print(subtract(20, 5))
print(math_utils.square(12))

# String Utils
print(string_utils.capitalize_words("hello world"))
print(string_utils.reverse_string("Python"))
print(string_utils.word_count("I love Python"))

print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))

total = calculate_total([100, 200, 300])

print(total)
print(apply_tax(total))