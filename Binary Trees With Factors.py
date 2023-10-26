class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        dp = [1] * n

        index = {x: i for i, x in enumerate(arr)}

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:  # arr[j] is a factor of arr[i]
                    other_factor = arr[i] // arr[j]
                    if other_factor in index:
                        dp[i] += dp[j] * dp[index[other_factor]]
                        dp[i] %= MOD

        return sum(dp) % MOD

# Example usage:
arr1 = [2, 4]
solution = Solution()
output1 = solution.numFactoredBinaryTrees(arr1)
print(output1)  # Output: 3

arr2 = [2, 4, 5, 10]
output2 = solution.numFactoredBinaryTrees(arr2)
print(output2)  # Output: 7
