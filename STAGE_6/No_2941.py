# https://www.acmicpc.net/problem/2941
# č	     c=
# ć	     c-
# dž     dz=
# đ	     d-
# lj  	 lj
# nj   	 nj
# š	     s=
# ž	     z=


import sys
input = sys.stdin.readline
print = sys.stdout.write

word = input().rstrip()
lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
rest = len(word)
n = 0

# 리스트 속 해당 문자열이 있는 개수만큼 더하기
# 그리고 리스트 속 해당 문자열 길이와 개수의 곱을 빼주기
for symbol in lst:
    if symbol in word:
        n += word.count(symbol)
        rest -= len(symbol) * word.count(symbol)
# "dz="과 "z="의 중복 없애기 : "dz="의 개수가 무조건 두 배가 됨
# 나머지 알파벳 수도 중복때문에 줄어들었으니 보충하기
# 나머지 알파벳 개수 더해주기
n -= word.count("dz=")
rest += len("z=") * word.count("dz=")
n += rest

print("%d" % n)