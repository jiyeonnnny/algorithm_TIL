```py
def break_arr(arr, x,y, cnt):
    global w,h
    q = [[x,y,arr[x][y]]]
    arr[x][y]=0
    remove_cnt = 0

    while q:
        x,y,tmp = q.pop(0)
        for p in range(1,tmp):
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx = x + dx*p
                ny = y + dy*p
                if 0<=nx<h and 0<=ny<w:
                    if arr[nx][ny] == 1:
                        arr[nx][ny] = 0
                        remove_cnt+=1
                    elif arr[nx][ny]>1:
                        q.append([nx, ny, arr[nx][ny]])
                        arr[nx][ny] = 0
                        remove_cnt += 1

    # print()
    # print('test')
    # print(x,y)
    # print('break-arr')
    # for a in arr:
    #     print(a)

    return arr, cnt-remove_cnt

def change_arr(arr):
    for j in range(w):
        i = h-1
        while i>=0:
            if arr[i][j]==0:
                k = i-1
                while k>=0:
                    if arr[k][j]:
                        arr[i][j],arr[k][j] = arr[k][j],arr[i][j]
                        break
                    k-=1
            i-=1

    # print('change arr')
    # for a in arr:
    #     print(a)

    return arr

def count_not_zero(arr):
    tmp = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]:
                tmp+=1
    return tmp


def recursive(arr, depth, cnt):
    global n,w,h,mn
    if depth == n:
        mn = min(mn, count_not_zero(arr))

        # print('depth = n')
        # for a in arr:
        #     print(a)
        return

    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                ar, cnt = break_arr(arr, i, j, cnt)

                print()
                print(i,j)
                print('ar')
                for a in ar:
                    print(a)

                print('arr')
                for a in arr:
                    print(a)

                ar = change_arr(ar)
                if cnt==0:
                    mn = 0
                    continue
                # print('cnt', cnt)
                recursive(ar, depth+1, cnt)
                # arr 이전 arr 로 돌아올 수 있는가?
                # recursive return 했을 때
                # print(i,j)
                #




for t in range(1):
    n,w,h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    mn = 10000

    recursive(arr, 0, count_not_zero(arr))
    print(f'#{t+1} {mn}')
```
[해결하는 중]
