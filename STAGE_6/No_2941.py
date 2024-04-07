# https://www.acmicpc.net/problem/2941
# č	     c=
# ć	     c-
# dž     dz=
# đ	     d-
# lj  	 lj
# nj   	 nj
# š	     s=
# ž	     z=

# Better code
import sys
input = sys.stdin.readline

# Note that the order of "dz=" and "z=" is important
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().rstrip()

# By replacing the symbols with '_', we can solve this problem more easily!
for s in lst:
    word = word.replace(s, '_')

print(len(word))


# import sys
# # Simplify the name of the functions
# input = sys.stdin.readline
# print = sys.stdout.write

# # inputed string
# word = input().rstrip()
# # some Croatian alphabets replaced with symbols
# lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# # the number of rest alphabets except the symbols
# rest = len(word)
# # the total number of the Croatian alphabets
# n = 0

# # Add the number of symbols existing in the list
# # Subtract the product of the number of symbols in the list and the length of them from rest
# for symbol in lst:
#     if symbol in word:
#         n += word.count(symbol)
#         rest -= len(symbol) * word.count(symbol)
# # Exclude the overlapping addition of the numbers of "dz=" and "z="
# # the number of "dz=" is doubled
# # Add as much as the decline of the rest, caused by the overlapping addition
# # Add the number of the rest alphabets to n
# n -= word.count("dz=")
# rest += len("z=") * word.count("dz=")
# n += rest

# # Note that sys.stdout.write() argument must be str, not int
# print("%d" % n)