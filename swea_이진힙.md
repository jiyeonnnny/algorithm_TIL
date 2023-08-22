```py
for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))[::-1]
    tree = [0]
    idx = 1
    node = 0

    while nums:
        node = nums.pop()
        tree.append(node)
        if 0<idx//2<=n and tree[idx//2] > tree[idx]:
            tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
        idx+=1

    idx = n
    ans = 0
    while 0<idx<n+1:
        idx//=2
        ans += tree[idx]
    print(f'#{t+1} {ans}')
```
[틀렸습니다]
- 틀린 이유: append해준 값이 부모노드와 비교하여 swap하는 건 맞는데, 그걸 한번만 하면 안됨
- 그 위의 부모노드가 크다면 한번 더 바꿔줘야함
- 부모노드가 작을때 까지 혹은, 부모 노드가 있을 때 까지 반복해야함

<br>
<br>
<br>

```py
for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))[::-1]
    tree = [0]
    idx = 1
    node = 0

    while nums:
        node = nums.pop()
        tree.append(node)
        idx = len(tree)-1
        while idx!=0 and tree[idx//2] > tree[idx]:
            tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
            idx//=2

    idx = n
    ans = 0
    while 0<idx<n+1:
        idx//=2
        ans += tree[idx]
    print(f'#{t+1} {ans}')
```
[SUCCESS]
