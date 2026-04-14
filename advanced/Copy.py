import copy
"""
赋值 (=)：完全不拷贝。只是给同一个对象贴了一个新标签
浅拷贝 (copy.copy / [:])：只拷贝第一层。外壳是新的，但里面的数据（子元素）依然是引用的旧地址
深拷贝 (copy.deepcopy)：完全递归拷贝。连根拔起，外壳和里面所有的子元素都是全新的，与原对象彻底断绝关系
"""

a = [1,2,3,[1,2,3]]
b = a
print(id(a)==id(b))#True

c = copy.copy(a) #切片法:c = a[:],效果一样
print(id(c)==id(a))#False
print(id(c[3])==id(a[3]))#True,因为子列表的地址依旧是的是旧的

d = copy.deepcopy(a)
print(id(d)==id(a))#False
print(id(d[3])==id(a[3]))#False