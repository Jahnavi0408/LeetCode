
class Solution:
    def bfs(self,status,candies,keys,newboxes,boxes,n):
        queue=deque([])
        for b in boxes:
            if status[b]==1:
                queue.appendleft(b)
            else:
                queue.append(b)
        
        ans=0
        have_keys=set()
        
        while queue:
            box=queue.popleft()
            
            if status[box]==1 or box in have_keys:
                ans+=candies[box]
                
                for k in keys[box]:
                    have_keys.add(k)
                    
                for b in newboxes[box]:
                    if status[b]==1 or b in have_keys:
                        queue.appendleft(b)
                    else:
                        queue.append(b)   
            else:
                break
            
        return ans
        
        
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], newboxes: List[List[int]], boxes: List[int]) -> int:
        n=len(status)    
    
        return self.bfs(status,candies,keys,newboxes,boxes,n)        
