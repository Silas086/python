# 快速把两个列表合并成字典
keys = ['name', 'age', 'job']
values = ['Skyler', 19, 'Engineer']

Dict = {k:v for k,v in zip(keys,values)} #{'name': 'Skyler', 'age': 19, 'job': 'Engineer'}
