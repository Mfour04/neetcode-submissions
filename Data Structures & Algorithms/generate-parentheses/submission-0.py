class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur, open, close):
            if len(cur) == 2*n:
                res.append("".join(cur))
                return
            
            if open < n:
                cur.append("(")
                dfs(cur, open + 1, close)
                cur.pop()
            
            if close < open:
                cur.append(")")
                dfs(cur, open, close + 1)
                cur.pop()

        dfs([], 0, 0)
        return res
