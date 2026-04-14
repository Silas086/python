# 给定一个由单词和空格组成的字符串，返回字符串中最后一个单词的长度。
# 输入： s = "Hello World"
# 输出： 5
# 说明：最后一个单词是长度为 5 的 "World"。

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])

s = Solution()
answer = s.lengthOfLastWord("Hello Worlda")
print(answer)