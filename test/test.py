# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 输入: "()[]{}"
# 输出: true
#
# 输入: "([)]"
# 输出: false
#
# 输入: "{[]}"
# 输出: true

# class Solution:
#     def isValid(self, s: str) -> bool:
#         dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
#         stack = ['?']
#         for c in s:
#             if c in dic: stack.append(c)
#             elif dic[stack.pop()] != c: return False
#         return len(stack) == 1
#
# s = Solution()
# print(s.isValid("()[]{}"))
# print(s.isValid("([)]"))
# print(s.isValid("{[]}"))

# 获取2天前的时间
# import time
# now = time.time()
# before_two_day = now - 60*60*24*2
# print(time.strftime("%Y-%m-%d %H:%m:%S",time.localtime(before_two_day)))
# print(time.asctime())

import urllib.request
responce = urllib.request.urlopen("http://www.baidu.com")
print(responce.status)