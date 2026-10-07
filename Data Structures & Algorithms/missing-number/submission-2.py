class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        store=set(range(0,n+1))
        for num in nums:
            store.discard(num)
        nu=list(store)
        return nu[0]