
k=int(input())
n= int(input())
lanterns = list(map(int,input().split()))


max_brightness = []

for i in range(len(lanterns) - k + 1):
    max_brightness.append(max(lanterns[i:i+k]))

print(min(max_brightness))