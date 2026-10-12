class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, cur = [], []
        
        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return 
            
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    cur.append(substring)
                    dfs(j + 1)
                    cur.pop()
        dfs(0)
        return res
