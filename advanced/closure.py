"""
def account_create(current_money = 0):
    def atm(num,flag = True):
        nonlocal current_money #可以对current_money进行修改
        if flag:
            current_money += num
            print(f"current money:{current_money}")
        else:
            current_money -= num
            print(f"current money:{current_money}")
    return atm
p1 = account_create(100) #拿到atm对象
p1(100)
p1(200)
p1(50,False)
"""

#实时平均值计算器
#我们需要计算一个数据流的实时平均值,
#传统的写法可能需要创建一个类（Class）或者使用全局变量来保存历史数据，但这样有点“重”。请使用闭包来实现
#每次调用 averager(value) 时，它应该把 value 加入计算，并返回当前所有历史输入值的平均值
def make_averager():
    #选择只记住count和total而不是用列表（因为列表会越来越大）可以节省空间
    count = 0
    total = 0
    def averager(value):
        #nonlocal用于在内部函数中修改外部函数的局部变量
        nonlocal count,total
        count += 1
        total += value
        return total/count

    return averager


avg = make_averager()
print(avg(10))
print(avg(20))
print(avg(30))