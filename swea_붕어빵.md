```py
def fish_bread():
    global arr
    Time = 0
    all_fish = 0
    custumer = arr.pop()
    while arr:
        Time+=1
        if Time%m==0:
            all_fish+=k
        if Time==custumer:
            if all_fish:
                all_fish-=1
                custumer = arr.pop()
            else:
                return 0
    return 1

for t in range(int(input())):
    n,m,k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    if fish_bread():
        print(f'#{t+1} Possible')
    else:
        print(f'#{t+1} Impossible')
```
[시간초과 - arr배열 순환으로 바꿈]

<br>
<br>

```py
def fish_bread():
    global arr, n
    for i in range(n):
        fishbread = (arr[i]//m)*k-(i+1)
        if fishbread<=0:
            return 0
    return 1

for t in range(int(input())):
    n,m,k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    if fish_bread():
        print(f'#{t+1} Possible')
    else:
        print(f'#{t+1} Impossible')
```
[틀렸습니다 - 1000개중에 996개 pass]
- 원인: 붕어빵 개수는 이미 현재 손님이 붕어빵을 가져간 개수 이므로, 가져간 후 붕어빵이 0인 것을 포함하면 안됨

<br>
<br>

```py
def fish_bread():
    global arr, n
    for i in range(n):
        fishbread = (arr[i]//m)*k-(i+1)
        if fishbread<0:
            return 0
    return 1

for t in range(int(input())):
    n,m,k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    if fish_bread():
        print(f'#{t+1} Possible')
    else:
        print(f'#{t+1} Impossible')
```
[SUCCESS]
