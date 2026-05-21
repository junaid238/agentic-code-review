class Solution:
    def reverse(self, x: int) -> int:
        sx = str(x)
        rsx = sx[::-1]
        if x>0:
            return int(rsx)
        else:
            rsx = rsx[:len(rsx)-1]
            return int("-"+rsx[:len(rsx)])

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
