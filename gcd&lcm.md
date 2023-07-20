```(python)
def gcd(x,y):
    while y!=0:
        x,y = y,x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)
```
