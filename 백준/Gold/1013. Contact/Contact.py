import re
import sys

inputText = int(sys.stdin.readline())

result = list()

for _ in range(inputText):
    temp = sys.stdin.readline().replace('\n','')
    pattern = re.compile('(100+1+|01)+')
    m = pattern.fullmatch(temp)
    if m : result.append('YES')
    else: result.append('NO')

for r in result:
   sys.stdout.write(str(r)+'\n')