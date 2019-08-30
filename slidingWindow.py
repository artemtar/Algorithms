def maxSlide(nums, k):
        if not nums or k == 0:
            return []
        stack = []
        res = []
        for i, j in enumerate(nums):
            while stack and nums[stack[-1]] < j:
                stack.pop(-1)
            if stack and stack[0] < i - k + 1:
                stack.pop(0)
            stack.append(i)
            if i >= k - 1:
                res.append(nums[stack[0]])
        return res