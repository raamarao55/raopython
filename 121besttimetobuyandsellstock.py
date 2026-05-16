#Brute force

prices = [7,1,5,3,6,4]

n = len(prices)
ans = 0

for i in range(n):
    for j in range(i+1, n):
        if prices[i] < prices[j]:
            temp = prices[j]-prices[i]
            ans = max(ans, temp)
print(ans)