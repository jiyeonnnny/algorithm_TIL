```py
def mid_tour(v):
    if 0<v*2<=n:
        mid_tour(v*2)
    print(v,end=' ')
    if 0<v*2+1<=n:
        mid_tour(v*2+1)

for t in range(int(input())):
    n = int(input())
    tree = [0]*(n+1)
    mid_tour(1)
```
[문제의 코드]
- 수정을 어떻게 해야할지 모르겠음

<br>
<br>
<br>

```py
def mid_tour(v):
    global depth

    if v>n:
        return

    mid_tour(v*2)
    depth+=1
    tree[v]=depth
    mid_tour(v*2+1)

for t in range(int(input())):
    n = int(input())
    tree = [0]*(n+1)
    depth=0
    mid_tour(1)
    print(*tree)
```
[정답 코드]
- 공부하기
- 아직 원리 이해 못함
