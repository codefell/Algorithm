class Solution:
    def _gen(self, n):
        if n == 0 and len(self.stack) == 0:
            self.ret.append(''.join(self.current))
        if n > 0:
            self.current.append('(')
            self.stack.append(')')
            self._gen(n - 1)
            self.current.pop()
            self.stack.pop()
        if len(self.stack) > 0:
            self.current.append(')')
            self.stack.pop()
            self._gen(n)
            self.current.pop()
            self.stack.append(')')
            
    def generateParenthesis(self, n):
        self.ret = []
        self.stack = []
        self.current = []
        self._gen(n)
        return self.ret

s = Solution()

print(s.generateParenthesis(4))