# def lengthOfLongestSubstring(s: str) -> int:
#     chars = []
#     for c in s:
#         # print(c)
#         if c not in chars:
#             chars.append(c)
#             # print(chars)
#         else:
#             print(c)

#     return len(chars)

# print(lengthOfLongestSubstring("abcabcbb"))
def lengthOfLongestSubstring(s: str) -> int:
    charset = set()
    l = 0
    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l = l+1 
        charset.add(s[r])
    return len(charset)

lengthOfLongestSubstring("babad")