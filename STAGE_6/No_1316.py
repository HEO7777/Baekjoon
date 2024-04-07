import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
# 코드길이 줄이기 : 전체 개수에서 아닌 개수만큼 줄여나가서 답을 찾는 방식
# 이렇게 하면 isTrue와 같은 변수들 사용할 필요 X -> 뒤의 if문도 없어져서 코드 길이 확 줄어듦
cnt = n

for _ in range(n):
    word = input().rstrip()
    # 와우, range()범위를 (0,0)과 같이 한번도 안돌게 하면 오류가 아니라
    # 그냥 한 번도 안돌고 지나감!!
    for j in range(len(word)-1):
        # 영어 소문자만 있어서 다행이지, 아니었으면
        # 내가 짠 알고리즘은 길이 100에다가 모두 서로다른 문자였으면 시간복잡도 겁나 길어짐
        # 근데 이 알고리즘은 그런 경우에도 한번만 돌면 되도록 해놓음 -> GOOD!!
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print("%d" % cnt)



# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# n = int(input())
# # 코드길이 줄이기 : 전체 개수에서 아닌 개수만큼 줄여나가서 답을 찾는 방식
# # 이렇게 하면 isTrue와 같은 변수들 사용할 필요 X -> 뒤의 if문도 없어져서 코드 길이 확 줄어듦
# tot = n

# for _ in range(n):
#     word = input().rstrip()
#     while len(word) != 0:
#         dum = word[0]
#         word = word.lstrip(dum)
#         if dum in word:
#             tot -= 1
#             break

# print("%d" % tot)



# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# n = int(input())
# tot = 0

# for _ in range(n):
#     isgrp = True
#     word = input().rstrip()
#     while len(word) != 0:
#         dum = word[0]
#         word = word.lstrip(dum)
#         if dum in word:
#             isgrp = False
#             break
#     if isgrp == True:
#         tot += 1

# print("%d" % tot)
