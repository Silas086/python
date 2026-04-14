#生成器 (Generator) 是一种特殊的迭代器 (Iterator)，而迭代器是一种特殊的“可迭代对象” (Iterable)
#凡是能丢进 for 循环里的东西，都是可迭代对象

#迭代器:
#迭代是 Python 最强大的功能之一，是访问集合元素的一种方式
#迭代器是一个可以记住遍历的位置的对象
#迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
#迭代器有两个基本的方法：iter() 和 next()

nums = [1, 2, 3] # Iterable
nums_iter = iter(nums) #创建迭代器对象
print(nums_iter) #<list_iterator object at 0x1094f7250>
print(next(nums_iter)) # 1
print(next(nums_iter)) # 2
print("-----------------")

#专业术语：生成器是一种特殊的迭代器，它惰性求值 (Lazy Evaluation)
#它不会一次性把所有结果算出来，而是保存算法状态，每次只算一个

#只要一个函数里出现了 yield 关键字，它就不再是普通函数，而是生成器函数
def make_cookies(n):
    print("🍪 厨师开始工作了...")
    for i in range(n):
        # yield 相当于 "暂停并送出结果"
        yield f"第 {i+1} 块饼干"
        print("--- 厨师休息中，等待下一个指令 ---")

# 调用函数时，它不会立即执行,而是返回一个生成器对象
chef = make_cookies(3)
print(chef) 
print(next(chef)) #<generator object make_cookies at 0x102906a80>
print(next(chef))
print(next(chef))
print("-----------------------\n")

#生成器表达式(把列表推导式的方括号 [] 换成圆括号() )
aaa = (x*x for x in range(10)) 
print(aaa) #<generator object <genexpr> at 0x1047bab50>
print(next(aaa)) #0
print(next(aaa)) #1
print(next(aaa)) #4
print(next(aaa)) #9
print("-----------------\n")

#用for循环使用生成器来获取里面的值
#attention:生成器是一次性的,遍历完一次后就空了。如果你想再遍历一次，必须重新创建一个新的生成器对象
#所以要写两遍chef = make_cookies(3)
chef = make_cookies(3)
for cookie in chef:
    print(f"我吃到了: {cookie}")
print("---------------\n")

#处理无限数据流:
def fibonacci():
    a, b = 0, 1
    while True: 
        yield a
        a, b = b, a + b

f = fibonacci()
for i in range(5):#想拿几个拿几个
    print(next(f))

#      return	                   yield 
#动作	 停止函数，交回控制权	       暂停函数，交回控制权
#状态	 函数结束，局部变量销毁	       函数挂起，保留局部变量状态
#次数	 一个函数只能 return 一次	  一个函数可以 yield 无数次

