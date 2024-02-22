fib = [(1, 0), (0, 1)]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(fib), n + 1):
        fib.append((fib[i - 1][0] + fib[i - 2][0], fib[i - 1][1] + fib[i - 2][1]))
    print(fib[n][0], fib[n][1])
