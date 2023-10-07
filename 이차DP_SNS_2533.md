[배운 점]
- 이차 DP 사용법

[주의 사항]
- 파이썬 억까 문제
- sys.setrecursionlimit(1000000)
- input = sys.stdin.readline
- python3 로 제출해야 통과함

```py
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node):
    visit[node]=1
    dp[node][1]=1

    for nxt in graph[node]:
        if not visit[nxt]:
            dfs(nxt)
            dp[node][0] += dp[nxt][1]
            dp[node][1] += min(dp[nxt][0],dp[nxt][1])

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [0]*(n+1)
dp = [[0,0] for _ in range(n+1)]
dfs(1)
print(min(dp[1]))
```
