# 2016. Maximum Difference Between Increasing Elements
#  Given a array of integers, find the maximum difference between two elements such that larger element appears after the smaller number.
nums = [7,1,5,4]

low = nums[0]
ans = -1

for i in range(1, len(nums)):
    if low < nums[i]:       
        temp = nums[i] - low
        ans = max(ans, temp)
    low = min(low, nums[i])
print(ans)

# Brute Force
nums = [7,1,5,4]
n = len(nums)
ans = -1
for i in range(n):
    for j in range (i+1, n):
        if nums[i] < nums[j]:
            temp = nums[j] - nums[i]
            ans = max(ans, temp)
print(ans)