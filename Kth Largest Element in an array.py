class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq,-1*nums[i])
        l = k-1
        while l > 0:
            heapq.heappop(pq)
            l = l-1
        return -1*pq[0]
