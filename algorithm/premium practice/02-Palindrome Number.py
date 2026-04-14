#给定一个整数x，true如果x是一个整数则返回。回文以及false其他情况
#输入： x = 121
#输出： true
#解释： 121 从左到右读作 121，从右到左读作 121
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        x2 = x1[::-1]
        if x2 == x1:
            return True
        else:
            return False
s = Solution()
result = s.isPalindrome(121)
print(result)