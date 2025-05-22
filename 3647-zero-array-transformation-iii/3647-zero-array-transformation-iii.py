class Solution:
    def maxRemoval(self, nums, queries):
 
        n, decr, idx = len(nums), 0, 0
        q = ans = len(queries)

        arr, heap = [0] * (n + 1), []
        queries.sort(key=lambda x: x[0])

        for i, num in enumerate(nums):
            decr-= arr[i]
            num-= decr

            while q > idx and queries[idx][0] == i:
                heappush(heap, (-queries[idx][1]))  
                idx+= 1

            while num > 0 and heap and -heap[0] >= i:
                arr[1 - heappop(heap)]+= 1
                ans-= 1
                decr+= 1
                num-= 1

            if num > 0: return -1
 
        return ans