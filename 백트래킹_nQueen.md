# nQueen

```py
import sys
input = sys.stdin.readline
d = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

def check(lst):
    global n
    for i in range(n): # i=x lst[i]=y
        x = i
        y = lst[i]
        for p in range(1,n+1):
            for dx,dy in d:
                nx = x + dx*p
                ny = y + dy*p
                if 0<=nx<n and 0<=ny<n:
                    if lst[nx]==ny:
                        return False
    return True

def nPn(lst):
    global n, ans
    if len(lst)==n:
        if check(lst[:]):
            ans += 1
            return
        return
    for i in range(1,n+1):
        if not visit[i-1]:
            visit[i-1]=1
            lst.append(i)
            nPn(lst)
            lst.pop()
            visit[i-1]=0


n = int(input())
ans = 0
visit = [0]*n
nPn([])
print(ans)
```
[시간초과]
- 8방향 해줄 필요 없음  2방향만 해도 됨
- 범위벗어나면 바로 break해줄 수 있게
- map visit 2차원 배열 만들어서 확인
- list 복사 안해도 됨

<br>
<br>
<br>

```py
import sys
input = sys.stdin.readline
d = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

def check(lst,map_visit):
    global n
    for i in range(n):
        x = i
        y = lst[i]
        if map_visit[x][y]==-1:
            return False
        map_visit[x][y] = 1
        for p in range(1,n+1):
            for dx,dy in d:
                nx = x + dx*p
                ny = y + dy*p
                if 0<=nx<n and 0<=ny<n:
                    if lst[nx]==ny or map_visit[nx][ny]==1:
                        return False
                    else:
                        map_visit[nx][ny]=-1
    return True

def nPn(lst):
    global n, ans
    if len(lst)==n:
        map_visit = [[0]*n for _ in range(n)]
        for i in range(n):
            map_visit[i][lst[i]] = 1
        if check(lst[:],map_visit):
            ans += 1
            return
        return
    for i in range(n):
        if not visit[i]:
            visit[i]=1
            lst.append(i)
            nPn(lst)
            lst.pop()
            visit[i]=0

n = int(input())
ans = 0
visit = [0]*n
nPn([])
print(ans)
```
- 1번코드에서 map 2차원 배열 만들어서 바로 check함

<br>
<br>
<br>

```py
import sys
input = sys.stdin.readline
d = [[1,1],[1,-1],[-1,1],[-1,-1]]

def check(arr,map_visit):
    for i in range(n):
        x = i
        y = arr[i]
        if map_visit[x][y]==1:
            return False
        
        for dx,dy in d:
            for p in range(1,n+1):
                nx = x + dx*p
                ny = y + dy*p
                if 0<=nx<n and 0<=ny<n:
                    if arr[nx]==ny:
                        return False
                    map_visit[x][y]=1
                else:
                    break
    return True


def recursive(lst):
    global ans 
    if len(lst)==n:
        map_visit = [[0]*n for _ in range(n)]
        if check(lst[:],map_visit):
            ans +=1
        return 
    
    for i in range(n):
        if not visit[i]:
            visit[i]=1
            lst.append(i)
            recursive(lst)
            lst.pop()
            visit[i]=0

n = int(input())
visit = [0]*n
ans = 0
recursive([])
print(ans)
```
- 1번 코드에서, 4방향으로 바꿈
- 범위 벗어나면 break
- 퀸이 지나가는 길에 다른 퀸 있으면 return
- 퀸이 지나가는 길을 표시

<br>
<br>
<br>

```py
import sys
input = sys.stdin.readline
d = [[1,1],[-1,1]]

def check(arr,map_visit):
    for i in range(n):
        x = i
        y = arr[i]
        if map_visit[x][y]==1:
            return False
        
        for dx,dy in d:
            for p in range(1,n+1):
                nx = x + dx*p
                ny = y + dy*p
                if 0<=nx<n and 0<=ny<n:
                    if arr[nx]==ny:
                        return False
                    map_visit[x][y]=1
                else:
                    break
    return True


def recursive(lst):
    global ans 
    if len(lst)==n:
        map_visit = [[0]*n for _ in range(n)]
        if check(lst,map_visit):
            ans +=1
        return 
    
    for i in range(n):
        if not visit[i]:
            visit[i]=1
            lst.append(i)
            recursive(lst)
            lst.pop()
            visit[i]=0

n = int(input())
visit = [0]*n
ans = 0
recursive([])
print(ans)
```
- 마지막코드에서, 2방향으로 바꿔줌

<br>
<br>
<br>

```py
import sys
input = sys.stdin.readline

def check(i,j,lst):
    for x in range(i):
        if abs(i-x) == abs(j-lst[x]):
            return False
    return True

def nPn(lst):
    global n, ans
    if len(lst)==n:
        ans += 1
        return
    for i in range(n):
        if not visit[i] and check(len(lst), i, lst):
            visit[i]=1
            lst.append(i)
            nPn(lst)
            lst.pop()
            visit[i]=0


n = int(input())
ans = 0
visit = [0]*n
nPn([])
print(ans)
```
- 퀸을 놓을때 check해주면서 퀸을 놓음
- SUCCESS

<br>
<br>
<br>
