# SWEA_BFS 홈 방법 서비스
---
```py
from collections import deque
d = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x,y,depth):
    house = 0
    q = deque([[x,y,1]])
    if arr[x][y]:
        house+=1
    visit[x][y] = 1
    while q:
        x,y,dp = q.popleft()
        if dp == depth:
            return house
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                q.append([nx,ny,dp+1])
                visit[nx][ny] = 1
                if arr[nx][ny]:
                    house += 1
    return house

for t in range(int(input())):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans_house = 0
    for i in range(n):
        for j in range(n):
            for k in range(1,2*n):
                visit = [[0]*n for _ in range(n)]
                tmp = bfs(i,j,k)
                price = tmp*m - k**2 - (k-1)**2
                if price>=0 and ans_house<tmp:
                    ans_house = tmp
    print(f'#{t+1} {ans_house}')
```
[시간초과]
- 아마 visit 때문일 듯
- for k문을 안에 넣는 방법 고안

<br>
<br>
<br>

```py
from collections import deque
d = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x,y):
    global ans
    house = 0
    if arr[x][y]:
        house+=1
    price = 0
    q = deque([[x,y]])
    visit = [[0]*n for _ in range(n)]
    visit[x][y] = 1
    depth = 1
    while q:
        x,y = q.popleft()

        if visit[x][y] == 2*n:
            return

        if visit[x][y] == depth+1:
            depth+=1
            price = house*m - visit[x][y]**2 - (visit[x][y]-1)**2
            if price>=0:
                ans = max(ans, house)

        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                q.append([nx,ny])
                visit[nx][ny] = visit[x][y] + 1
                if arr[nx][ny]:
                    house+=1

    return

for t in range(int(input())):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            bfs(i,j)
    print(f'#{t+1} {ans}')
```
[틀렸습니다]
- ans 초기값
- house 1개 일때

<br>
<br>
<br>

```py
from collections import deque
d = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x,y):
    global ans
    house = 0
    if arr[x][y]:
        house+=1
        ans = max(ans,1)
    q = deque([[x,y]])
    visit = [[0]*n for _ in range(n)]
    visit[x][y] = 1
    depth = 1
    while q:
        x,y = q.popleft()
        if visit[x][y] == 2*n:
            return visit
        if visit[x][y] == depth+1:
            depth+=1
            price = house*m - visit[x][y]**2 - (visit[x][y]-1)**2
            if price>=0:
                ans = max(ans, house)
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                q.append([nx,ny])
                visit[nx][ny] = visit[x][y] + 1
                if arr[nx][ny]:
                    house+=1
    return visit

for t in range(int(input())):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            visit = bfs(i,j)
    print(f'#{t+1} {ans}')
```
[PASS]
