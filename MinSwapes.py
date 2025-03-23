
n = int(input().strip())
a = list(input().strip())
b = list(input().strip())

if len(a) != len(b):
    print(-1)
    exit()

swaps = 0
for i in range(n):
    if i not in a:
        print(-1)
        exit()
    j = a.index(b[i])  
    while j > i:
        a[j], a[j - 1] = a[j - 1], a[j]
        swaps += 1
        j -= 1

print(swaps)
