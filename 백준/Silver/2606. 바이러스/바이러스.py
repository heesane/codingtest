## 2606 바이러스
## 15:00

computer = int(input())
network = int(input())

computer_list = [False for _ in range(computer+1)]

dfs_list = [[] for _ in range(computer+1)]

for _ in range(network):
    a, b = map(int, input().split())
    dfs_list[a].append(b)
    dfs_list[b].append(a)
    
def dfs(start, dfs_list, computer_list):
    computer_list[start] = True
    for i in dfs_list[start]:
        if not computer_list[i]:
            dfs(i, dfs_list, computer_list)

dfs(1,dfs_list,computer_list)
print(computer_list.count(True)-1)