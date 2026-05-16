#Brute Force
colors = [1,1,1,6,1,1,1]
n = len(colors)
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if(colors[i] != colors[j]):
            temp = j-i
            ans = max(ans, temp)
print(ans)

# Optimized

colors = [1,1,1,6,1,1,1]
n = len(colors)
ans = 0

for i in range(n-1,-1,-1):
    if(colors[i] != colors[0]):
        temp = i-0
        ans = max(ans, temp)
        break
for i in range(n):
    if(colors[i] != colors[n-1]):
        temp = n-1-i
        ans = max(ans, temp)
        break
print(ans)