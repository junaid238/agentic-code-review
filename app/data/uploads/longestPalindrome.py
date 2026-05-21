# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         chars = []
#         for i in range(len(s)):
            
#             for j in range(i+1,len(s)+1):
#                 # print(s[i:j])
#                 if s[i:j] == s[i:j][::-1]:  
#                     chars.append(s[i:j])
#         return (max(chars, key=len))
                
# sol= Solution()
# sol.longestPalindrome("babad")

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        lenres = 0
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > lenres:
                    res = s[l:r+1]
                    lenres = r-l+1
                l -= 1
                r += 1
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > lenres:
                    res = s[l:r+1]
                    lenres = r-l+1
                l -= 1
                r += 1
        return res

sol = Solution()
print(sol.longestPalindrome("babad"))