# 1193 분수찾기

target = int(input())

start = 1
    
while target > start:
    target -= start
    start += 1

if start % 2 == 0:
    print(f'{target}/{start - target + 1}')
else:
    print(f'{start - target + 1}/{target}')