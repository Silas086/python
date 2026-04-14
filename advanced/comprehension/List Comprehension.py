#场景：把一个列表里的数字都变成平方
list = [1,2,3,4]
list1 = [i*i for i in list]

#场景：只想要列表里的偶数
list2 = [x for x in list if x%2==0]

#场景：你从数据库读出来一堆字符串，有的有空格，有的又是大写又是小写。你需要统一格式
names = ["  Alice ", "Bob", "  cindy"]
Names = [name.strip().title() for name in names]
print(Names)

#有一个列表 price = [100, 50, 80, 200, 10]
#请生成一个新的列表，规则是：大于 60 的打九折，小于等于 60 的保持原价
price = [100, 50, 80, 200, 10]
new_price = [x*0.9 if x >60 else x for x in price]
print(new_price)
