# 백준 1924 2007년

N = input().split()

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

x = int(N[0])
y = int(N[1])

for i in range(1, x):
    if i == 2:
        y += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        y += 30
    else:
        y += 31

print(day[y % 7])
