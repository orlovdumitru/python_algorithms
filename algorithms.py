
data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

target = 27
# linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# print(linear_search(data, target))

# ======================================================================
# Iterative Binary search
def binary_search_iterative(data, target):
    low = 0
    high = len(data)

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

# print(binary_search_iterative(data, target))

# -------------------------------------------------------------
# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)
# print(binary_search_recursive(data, target, 0, len(data)-1))

# ================================================================

input_s_1 = 'joraPrograming'
input_s_2 = 'JoraPrograming'
input_s_3 = 'joraprograming'

# for search for upper characters
def find_uppercase_iterate(input_st):
    for i in range(len(input_st)):
        if input_st[i].isupper():
            return input_st[i]
    return "No uppercase found"

# print(find_uppercase_iterate(input_s_1))
# print(find_uppercase_iterate(input_s_2))
# print(find_uppercase_iterate(input_s_3))
# -----------------------------------------------------------------

# recursive find upper characters
def find_uppercase_recursive(input_st, idx=0):
    if input_st[idx].isupper():
        return input_st[idx]
    if idx == len(input_st) - 1:
        return "No uppercase found"
    return find_uppercase_recursive(input_st, idx+1)
# print(find_uppercase_recursive(input_s_1))
# print(find_uppercase_recursive(input_s_2))
# print(find_uppercase_recursive(input_s_3))
# =====================================================================

input_s_1 = 'SomeSimpleText'
# calculate string length iteration
def iterative_string_len(input_st):
    count = 0
    for i in input_st:
        count += 1
    return count
# print(iterative_string_len(input_s_1))
# ------------------------------------------------------------
# recursive string len count
def recursive_string_len(input_s_1):
    if input_s_1 == '':
        return 0
    return 1 + recursive_string_len(input_s_1[1:])
# print(recursive_string_len(input_s_1))
# =========================================================

input_st_1 = 'abc de'
input_st_2 = 'LuCiDProGrAmMiNG'
vowels = 'aeiou'
# count consonant
def consonant_counter_iterative(input_st):
    counter = 0
    for i in input_st:
        if i.isalpha() and i.lower() not in vowels:
            counter += 1
    return counter
# print(consonant_counter_iterative(input_st_1))
# print(consonant_counter_iterative(input_st_2))
# --------------------------------------------------------
def consonant_counter_recursive(in_str):
    if in_str == '':
        return 0
    if in_str[0].lower() not in vowels and in_str[0].isalpha():
        return 1 + consonant_counter_recursive(in_str[1:])
    else:
        return consonant_counter_recursive(in_str[1:])
# print(consonant_counter_recursive(input_st_1))
# print(consonant_counter_recursive(input_st_2))
# ========================================================

# Product of 2 mumbers
x = 3
y = 5
def product_number_iterate(a, b):
    nr = 0
    for i in range(a):
        nr += b
    return nr
# --------------------------------------------------------------
def product_number_recursive(a, b):
    if a == 0:
        return 0
    else:
        return b + product_number_recursive(a-1, b)
# print(product_number_iterate(x, y))
# print(product_number_recursive(x, y))
# ================================================================

# Look and say sequence
# 1
# 11
# 21
# 1211
# 111221
# 312211

def next_number(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while (i + count < len(s)) and (s[i + count] == s[i]):
            count += 1
        result = result + (str(count) + s[i])
        i = i + count
    return result

def next_number_sequence(begin, levels):
    for i in range(levels):
        # print(begin)
        begin = next_number(begin)
next_number_sequence('1', 10)
# ==============================================================

# Spreadsheet encoding
def spread_encode(in_str):
    result = ''
    str_len = len(in_str)
    start = ord('A') - 1
    for i in range(str_len):
        if i < str_len - 1:
            result += str( (ord(in_str[i].upper()) - start) * (26**(str_len-i-1) )) + '+'
        else:
            result += str( (ord(in_str[i].upper()) - start) * (26**(str_len-i-1) ))
    return eval(result)
# --------------------------------------------------------
# simpler version
def spread_encode_simple(in_str):
    str_len = len(in_str)
    start = ord('A') - 1
    num = 0
    for i in range(str_len):
        num += (ord(in_str[i].upper()) - start) * (26**(str_len-i-1) )
    return num

# print(spread_encode_simple('A'))
# print(spread_encode_simple('AA'))
# print(spread_encode_simple('ZZ'))
# ========================================================================

# Is Palindrome
def is_palindrome(in_srt):
    return in_srt == in_srt[::-1]
# ------------------------------------
# ignore case
def is_palindrome_ignore(in_str):
    s = ''.join([i for i in in_str if i.isalnum()]).replace(' ', '').lower()
    return s == s[::-1]

# print(is_palindrome_ignore('ana'))
# print(is_palindrome_ignore('banana'))
# print(is_palindrome_ignore('Was it a cat I saw?'))
# --------------------------------------------------------------
# less iteration
def is_palindrome_less(in_st):
    i = 0
    j = len(in_st) - 1
    
    while i < j:
        while not in_st[i].isalnum() and i < j:
            i += 1
        while not in_st[j].isalnum() and i < j:
            j -= 1
        if in_st[i].lower() != in_st[j].lower():
            return False
        i += 1
        j -= 1
    return True
# print(is_palindrome_less('Was it a cat I saw?'))
# print(is_palindrome_less('banana'))
# print(is_palindrome_less('ana'))
# ==================================================================

# Check if is anagram
