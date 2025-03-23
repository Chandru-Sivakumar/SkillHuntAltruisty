path = input().strip()
n = int(input())

treasures = []

for _ in range(n):
    start, end = map(int, input().split())
    treasures.append(path[start-1:end].count('T'))

for i in range(n):
    print(treasures[i])
