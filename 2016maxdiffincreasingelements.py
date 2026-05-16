#Brute force
prices = [7,1,5,4]

n = len(prices)
ans = -1

for i in range(n):
    for j in range(i+1,n):
        if prices[i] < prices[j]:
            temp = prices[j] - prices[i]
            ans = max(temp, ans)
print(ans)