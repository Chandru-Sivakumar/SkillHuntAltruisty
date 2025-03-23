n = int(input())

prices = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

max_profit = 0
i=0
while(i<n):
    j = i+1
    while(j<n):
        max_profit = max(max_profit, prices[j]-prices[i])
        j+=1
    i+=1
print(max_profit)