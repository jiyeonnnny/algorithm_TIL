```py
def bfs():
    q = deque([['J',jx,jy],['F',fx,fy]])
    while q:
        while q:
            ForJ, x, y = q.popleft()
            if ForJ=='F':
                q.appendleft(['F',x,y])
                break
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx = x + dx
                ny = y + dy
                if (nx==0 or nx==n-1 or ny==0 or ny==m-1) and arr[nx][ny]=='.':
                    visited[nx][ny] = visited[x][y] + 1
                    return visited[nx][ny]
                elif arr[nx][ny]=='.':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append(['J',nx,ny])
        while q:
            ForJ, x,y = q.popleft()
            if ForJ == 'J':
                q.appendleft([ForJ,x,y])
                break
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='.':
                    arr[nx][ny]='F'
                    q.append(['F',nx,ny])
    return -1

n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

jx,jy,fx,fy = 0,0,0,0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'J':
            jx,jy = i,j
            arr[i][j]='.'
            visited[i][j]=1
        if arr[i][j] == 'F':
            fx,fy = i,j
tmp = bfs()

if tmp==-1:
    print('IMPOSSIBLE')
else:
    print(tmp)
```
[틀렸습니다]
- 반례)
3 300
############################################################################################################################################################################################################################################################################################################
..........................................................................................................................................................................................................................................................................................................J#
############################################################################################################################################################################################################################################################################################################
299
- 불이 여러 개인 경우를 고려하지 못함

<br>
<br>

```py
def bfs():
    while q_J:
        for _ in range(len(q_J)):
            x, y = q_J.popleft()
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx = x + dx
                ny = y + dy
                if (nx==0 or nx==n-1 or ny==0 or ny==m-1) and arr[nx][ny]=='.' and visited[nx][ny]==0:
                    visited[nx][ny] = visited[x][y] + 1
                    return visited[nx][ny]

                if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='.' and visited[nx][ny]==0:
                    q_J.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1

        for _ in range(len(q_F)):
            x,y = q_F.popleft()
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='.':
                    arr[nx][ny]='F'
                    q_F.append([nx,ny])

    return -1


n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

q_F = deque([])
q_J = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'F':
            q_F.append([i, j])
        elif arr[i][j] == 'J':
            q_J.append([i, j])
            arr[i][j]='.'
            visited[i][j]=1

tmp = bfs()

if tmp==-1:
    print('IMPOSSIBLE')
else:
    print(tmp)
```
[50% 틀렸습니다]
- 원인: 불이 지훈이 위치에 도달했을 경우, impossible을 못함

<br>
<br>

```py
def bfs():
    while q_J:

        for _ in range(len(q_J)):
            x, y = q_J.popleft()

            if arr[x][y]=='F':
                continue

            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx = x + dx
                ny = y + dy

                if 0>nx or nx>=n or 0>ny or ny>=m:
                    return visited[x][y]

                # if (nx==0 or nx==n-1 or ny==0 or ny==m-1) and arr[nx][ny]=='.' and visited[nx][ny]==0:
                #     visited[nx][ny] = visited[x][y] + 1
                #     return visited[nx][ny]

                if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='.' and visited[nx][ny]==0:
                    q_J.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1

        for _ in range(len(q_F)):
            x,y = q_F.popleft()
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='.':
                    arr[nx][ny]='F'
                    q_F.append([nx,ny])

    return -1


n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

q_F = deque([])
q_J = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'F':
            q_F.append([i, j])
        elif arr[i][j] == 'J':
            q_J.append([i, j])
            arr[i][j]='.'
            visited[i][j]=1


tmp = bfs()
# print('arr')
# for a in arr:
#     print(a)
# print('visited')
# for v in visited:
#     print(v)


if tmp==-1:
    print('IMPOSSIBLE')
else:
    print(tmp)
```
[SUCCESS]
