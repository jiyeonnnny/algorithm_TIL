a = dict()
for i in range(5):
    a[i] = input().strip()

for i in range(15):
    for j in range(5):
        if len(a[j])>i:
            print(a[j][i],end='')