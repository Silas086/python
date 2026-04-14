"""
常用字符组:
\d : 数字 (Digit)。等价于 [0-9]
\D : 非数字
\w : 单词字符 (Word)。等价于 [a-zA-Z0-9_] (字母、数字、下划线)
\W : 非单词字符 (符号、空格等)
\s : 空白字符 (Space)。包括空格、制表符 \t、换行符 \n
\S : 非空白字符
.	通配符。匹配除换行符外的任意一个字符	
^	开始锚点。匹配字符串的开头
$	结束锚点。匹配字符串的结尾

常用量词:
* : 0 次或多次	
+ : 1 次或多次	
? : 0 次或 1 次	
{n} : 恰好 n 次	
{n,} : 至少 n 次	
{n,m} : n 到 m 次
"""

import re
a = "1234 444 232 1234"
#re.match方法:只检查字符串的开头。如果开头不匹配，就算后面有也不行。
result = re.match("1234",a) #<re.Match object; span=(0, 4), match='1234'>
result1 = re.match("234",a) #None

print(result.span()) #span=(0, 4)
print(result.group()) #match='1234'
print("-------------------")

b = '123abc AAAA'
result2 = re.search('3',b)
print(f"result2:{result2}") #<re.Match object; span=(2, 3), match='3'>
print("---------------------------")

c="AB ABa ABCD AAAA"
#re.findall:搜索整个字符串，以List形式返回所有匹配的字符串
print(re.findall("AB",c)) #['AB', 'AB', 'AB']

d="1234ABCD"
r = "[0-9a-zA-Z]"
result3 = re.findall(r,d) #['1', '2', '3', '4', 'A', 'B', 'C', 'D']

#匹配qq邮箱
def check(email):
    pattern = r"^[1-9]\d{9}@qq.com$"  #r防转义
    #^表示开头匹配一个数字[1-9], \d{9}表示任意数字出现9次,加上$表示结尾匹配@qq.com
    if re.findall(pattern,email):
        return True
    return False
 
if __name__ == "__main__":
    print(check("2256630439@qq.com")) #True
    print(check("22566@qq.com")) #False
    print(check("2256630439qq.com")) #False