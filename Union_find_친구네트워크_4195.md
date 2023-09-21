```py
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    parent = {}
    chilren = {}
    n = int(input())
    for _ in range(n):
        name1, name2 = input().strip().split()
        parent[name2] = name1
        chilren[name1] = name2

        start = name2
        while start in chilren.keys():
            start = chilren[start]
        
        ans = 1
        while start in parent.keys():
            ans += 1
            start = parent[start]
        print(ans)
```
[시간초과]
- 아마 start 지점 찾고, 다시 parent 찾는 과정에서 시간 초과 났을듯
- 그래서 union find 를 사용해야하는 거 같음
- 그리고 class Node를 사용하고 싶었는데, 사용할 수 없다고 함
- dictionary를 사용해야하고, 이름 str대신 int를 사용해야함

<br>
<br>
<br>

```py
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px>py:
        parents[px] = py
        cnt[py]+=cnt[px]
        cnt[px]=0
    elif px<py:
        parents[py] = px
        cnt[px]+=cnt[py]
        cnt[py]=0
    return

for _ in range(int(input())):
    d = {}
    num = 0
    parents = []
    cnt = []
    for _ in range(int(input())):
        name1, name2 = input().strip().split()
        if name1 not in d:
            d[name1] = num
            parents.append(num)
            cnt.append(1)
            num+=1
        if name2 not in d:
            d[name2] = num
            parents.append(num)
            cnt.append(1)
            num+=1
        union(d[name1], d[name2])
        print(cnt[0])
```
[틀렸습니다]
- 출력하는 cnt[0]에서 틀린 것 같았음
- name2의 조상노드의 cnt 값을 출력해야함
- 그래서 find함수를 사용해야함

<br>
<br>
<br>


```py
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px>py:
        parents[px] = py
        cnt[py]+=cnt[px]
    elif px<py:
        parents[py] = px
        cnt[px]+=cnt[py]
    return

for _ in range(int(input())):
    d = {}
    num = 0
    parents = []
    cnt = []
    for _ in range(int(input())):
        name1, name2 = input().strip().split()
        if name1 not in d:
            d[name1] = num
            parents.append(num)
            cnt.append(1)
            num+=1
        if name2 not in d:
            d[name2] = num
            parents.append(num)
            cnt.append(1)
            num+=1
        union(d[name1], d[name2])
        print(cnt[find(d[name2])])
```
[SUCCESS]

<br>
<br>
<br>
