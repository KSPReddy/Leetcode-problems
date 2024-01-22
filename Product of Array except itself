class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]
        post = [1]
        
        for i in range(0,n):
            res = nums[i]*pre[-1]
            pre.append(res)

        for i in range(n-1,-1,-1):
            res = nums[i]*post[0]
            post = [res] + post

        result=[]
        for i in range(0,n):
            out = pre[i]*post[i+1]
            result.append(out)
        return result