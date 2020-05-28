
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
s1 = 'fairy tales'
s2 = 'rail safety'
# s2 = 'rail safetyx'
s1 = s1.replace(' ', '').lower()
s2 = s2.replace(' ', '').lower()

# requires n log n time
# print( sorted(s1) == sorted(s2) )

def is_anagram(s1, s2):
    ht = {}

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht.values():
        if i != 0:
            return False
    return True
# print(is_anagram(s1, s2))
# =======================================================================

# Greedy Algorithms optimal Task 
a = [6, 3, 5, 2, 7, 5]
# lowest posible combintion number
def lowest_posible(arr):
    arr.sort()
    result = []
    for i in range(len(a)//2):
        result.append(arr[i] + arr[-i-1])
    return result
# print(lowest_posible(a))
# ========================================================================

# Intersection of 2 sorted arrays
a = [2, 3, 3, 5, 7, 11]
b = [3, 3, 7, 15, 31]

def intersect_array(a, b):
    result = []
    for i in a:
        if i in b and i not in result:
            result.append(i)
    return result

# ------------------------------------------------------------------

def intersect_sorted_array(a, b):
    i = 0
    j = 0
    intersection = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if i == 0 or a[i] != a[i-1]:
                intersection.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return intersection

# print(list(set(a).intersection(b)))
# print(intersect_sorted_array(a, b))
# =========================================================================

# Palindrome Permutation
palin_perm = 'Tact Coa!'
palin_perm1 = 'Tact Coa'
not_palin_perm = 'This is not a palindrome permutation'

def palindrome_permutation(in_str):
    in_str = in_str.replace(' ', '').lower()
    result = {}
    for i in in_str:
        if i.isalnum() and i in result:
            if result[i] > 0:
                result[i] -= 1
            else:
                result[i] += 1
        else:
            result[i] = 1
    c = 0
    for i in result.values():
        if i > 0:
            c += 1
        if c > 1:
            return False
    
    return True

# print(palindrome_permutation(palin_perm))
# print(palindrome_permutation(palin_perm1))
# =====================================================================

is_perm1 = 'God'
is_perm2 = 'dog'
not_perm1 = 'Not'
not_perm2 = 'top'

# check permutation
# O(n log n)
def is_perm_1(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            return False
    return True
# ------------------------------------------
# O(n)
def is_perm_2(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    d = {}
    for i in s1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    for i in s2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    return all(value == 0 for value in d.values())
    
# print(is_perm_1(is_perm1, is_perm2))
# print(is_perm_1(not_perm1, not_perm2))
# print(is_perm_2(is_perm1, is_perm2))
# print(is_perm_2(not_perm1, not_perm2))
# ==================================================================

# Uniq characters
unique_s = 'AbCDefG'
non_unique = 'non Unique STR'
def is_unique(in_str):
    d = {}
    in_str = in_str.replace(' ', '').lower()
    for i in in_str:
        if i in d:
            return False
        elif i.isalnum():
            d[i] = 1
    return True
# ----------------------------------------------------------
def is_unique_2(in_str):
    return len(set(in_str)) == len(in_str)
# ----------------------------------------------------------
def is_unique_3(in_str):
    in_str = in_str.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in in_str:
        if i in alpha:
            alpha = alpha.replace(i, '')
        else:
            return False
    return True

# print(is_unique_3(unique_s))
# print(is_unique_3(non_unique))
# =================================================================

# Find closest number
a = [1, 2, 4, 5, 6, 6, 8, 9]
a1 = [2, 5, 6, 7, 8, 8, 9]
def closest_num(ls, target):
    min_dif = float('inf')
    low = 0
    high = len(ls) - 1
    closest_n = None

    if len(ls) == 0:
        return None
    if len(ls) == 1:
        return ls[0]
    
    while low <= high:
        mid = (low + high) // 2
        if mid + 1 < len(ls):
            min_dif_right = abs(ls[mid+1] - target)
        if mid > 0:
            min_dif_left = abs(ls[mid-1] - target)

        if min_dif_left < min_dif:
            min_dif = min_dif_left
            closest_n = ls[mid - 1]
        
        if min_dif_right < min_dif:
            min_dif = min_dif_right
            closest_n = ls[mid + 1]
        
        if ls[mid] < target:
            low = mid + 1
        elif ls[mid] > target:
            high = mid - 1
        else:
            return ls[mid]
    return closest_n

# print(closest_num(a, 11))
# print(closest_num(a, -1))
# print(closest_num(a1, 6))
# ======================================================================

# O(n)
# find num which is on same index mumber
a1 = [-10, -5, 0, 3, 7]
a2 = [0, 2, 5, 8, 17]
a3 = [-10, -5, 3, 4, 7, 9]

def find_fixed_point_linear(ar):
    ls = []
    for idx, i in enumerate(ar):
        if i == idx:
            ls.append(i)
    return ls
# -----------------------------------------------

# O(log n)
# sorted list
def find_fixed_point_binary(ar):
    low = 0
    high = len(ar) - 1
    while low <= high:
        mid = (low + high) // 2

        if ar[mid] < mid:
            low = mid + 1
        elif ar[mid] > mid:
            high = mid - 1
        else:
            return ar[mid]
    return None
# print(find_fixed_point_binary(a1))
# print(find_fixed_point_binary(a2))
# print(find_fixed_point_binary(a3))
# ======================================================================

a1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
a2 = [1, 2, 3, 4, 1]
a3 = [1, 6, 5, 4, 3, 2, 1]
# Find Bitonic Peak
def find_highest_number(ar):
    low = 0
    high = len(ar) - 1

    if len(ar) < 3:
        return None
    while low <= high:
        mid = (low + high) // 2
        mid_left = ar[mid - 1] if mid - 1 > 0 else float('-inf')
        mid_right = ar[mid + 1] if mid + 1 < len(ar) else float('inf')

        if mid_left < ar[mid] and mid_right > ar[mid]:
            low = mid + 1
        elif mid_left > ar[mid] and mid_right < ar[mid]:
            high = mid - 1
        elif mid_left < ar[mid] and mid_right < ar[mid]:
            return ar[mid]
    return None
# print(find_highest_number(a1))
# print(find_highest_number(a2))
# print(find_highest_number(a3))
# =========================================================================

a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 285
# find first entry in list with duplicate
def find_first_idx(ar, target):
    low = 0
    high = len(ar) - 1

    while low <= high:
        mid = (low + high) // 2

        if ar[mid] < target:
            low = mid + 1
        elif ar[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if ar[mid - 1] != target:
                return mid
            else:
                high = mid - 1
    return -1
# print(find_first_idx(a, target))
# ==============================================================

# Python bisect method
import bisect
a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
# print(bisect.bisect_left(a, -10)) # first ocurance form left
# print(bisect.bisect_right(a, -10)) # first ocurance form right
# print(bisect.bisect_left(a, 285))# first ocurance form left
# print(bisect.bisect_right(a, 285)) # first ocurance form right
# print(bisect.bisect(a, 285)) # short fro bisect right
# -------------------------------------------------------------------------
# print(a)
bisect.insort_left(a, 108)
bisect.insort_right(a, 108)
bisect.insort_right(a, 285)
# print(a)
# =====================================================================

# Interget Square root
k = 12
def interger_square_root(val):
    low = 0
    high = val

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        if mid_squared < val:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1
# print(interger_square_root(k))
# ==================================================================

# Cyclically shifted array
a = [4, 5, 6, 7, 1, 2, 3]

def find_binary(ar):
    low = 0
    high = len(ar) - 1

    while low < high:
        mid = (low + high) // 2
        if ar[mid] > a[high]:
            low = mid + 1
        elif ar[mid] <= a[high]:
            high = mid
    return low

# print(find_binary(a))
# idx = find_binary(a)
# print(a[idx])
# ==========================================================================

# Convert number to string without using str()
def int_to_str(input_int: int) -> str:
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False
    
    output_str = []
    while input_int > 0:
        output_str.append(chr(ord('0') + input_int % 10))
        input_int //= 10
    
    result = ''.join(output_str)[::-1]
    if is_negative:
        result = '-' + result
    return result

# numb = 123520135201144
# print(int_to_str(numb))
# ========================================================================

# convert string to int
def str_to_int(input_str):
    output_int = 0
    if input_str[0] == '-':
        start = 1
        is_negative = True
    else:
        start = 0
        is_negative = False
    s_len = len(input_str)
    for i in range(start, s_len):
        nr = ord(input_str[i]) - ord('0')
        output_int += nr * (10 ** (s_len - i - 1))
    if is_negative:
        return (-1 * output_int)
    return output_int

# convert = '12352013121'
# convert = '-52013121'
# convert = '01'
# print(str_to_int(convert))