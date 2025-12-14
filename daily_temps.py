class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(nlogn) , sort based on temp, ignore index if index < current index
        # but its prolly O(n^2) in worst case
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans