#装饰器本质上是一个闭包函数

#decorator一般写法
def a(func):
    def b():
        print("hi")
        func()
    return b
def introduce():
    print("i am Georgeeeeee")
f1 = a(introduce)
f1()

#decorator快捷写法 (@语法糖)，可以实现自动赋值
def aaaaa(func):
    def b():
        print("hi")
        func()
    return b

@aaaaa
def introduce():
    print("i am George")
introduce()
print("----------------")

class A:
    name = "Q"
    #内置装饰器(无需访问对象属性)
    @staticmethod
    def staticmethod():
        print("hi")

    @classmethod
    def classmethod(cls):
        return cls.name
A.staticmethod()
A = A.classmethod()
print(A)