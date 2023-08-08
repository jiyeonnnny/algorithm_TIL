주의 사항
1. 재귀
2. 시간초과
3. 메모리초과

![rn_image_picker_lib_temp_8154d1dc-9f57-40e8-a215-15b7a8354ee4](https://github.com/jiyeonnnny/AlgorithmStudy/assets/139419091/e659636b-052f-47cf-94fa-78ad38154838)

<br>
<br>
<br>


```py
import sys
input = sys.stdin.readline

def recursive(a,b,c):
    if b==0:
        return 1
    elif b==1:
        return a%c

    tmp = recursive(a, b // 2, c)
    if b%2 == 0:
        return ((tmp%c) * (tmp%c)) %c
    else:
        return ((tmp%c) * ((tmp%c)*a%c)) %c

a,b,c = map(int, input().split())
print(recursive(a,b,c))
```
