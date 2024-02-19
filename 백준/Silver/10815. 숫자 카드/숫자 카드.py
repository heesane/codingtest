# 백준 10815 숫자카드
# 시간 초과 -> 이분 탐색

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def binary_search(n_list, target):
    start = 0
    end = len(n_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target:
            return 1
        elif n_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in m_list:
    print(binary_search(n_list, i), end=' ')
print()