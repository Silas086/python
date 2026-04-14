"""
场景：
假设你有一个很贵的 API 接口（或者一个付费功能），为了防止用户滥用，你需要限制某个函数只能被成功调用 3 次。
如果是前 3 次调用，正常执行原函数，并返回原函数的结果。
超过 3 次后,不再执行原函数,而是直接打印警告:“API配额已用完”,并返回 None。"""

#*args：负责把所有位置参数打包成一个元组（tuple）
#**kwargs：负责把所有关键字参数打包成一个字典（dict）
#目的:传入1，2个参数或者不传参也行
def limit(func):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        if count > 3:
            print("Failed")
        else:
            return func(*args,**kwargs)
    return inner

@limit
def a(x,y):
    print(f"计算{x}+{y}={x+y}")
a(1,2)
a(1,3)
a(1,4)
a(1,5)