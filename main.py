import re
p = re.compile(
    "[A-Z]{3,3}[0-9][A-Za-z0-9]{4,4}[A-Za-z0-9]{16,16}.\S{6,6}.\S{27,27}")


text = '''
예시
토큰
입니다
asdfasdfga
asdgfatygwetwt
aw
OTE4ODE5Mzg0MzkzMzUxMTg4.YbMzow.AghGMGdLpUWR3Wr400GNBuKWXt8
OTE4ODE5NzYwMDM5NDAzNTIw.YbMz7w.WkfWlfq1qnmAuJ_ZLDMLa34Rys4
fo1uze3n25@dollarnoob.com:qpwo12!@:OTE4ODE3Njg3NDU3NjYwOTc4.YbMx7A.BVwF7HtsY2fw7BXs8zFz_sEw6Vc
dgsy9eg65c@dollarnoob.com:qpwo12!@:OTE4ODE3NjkwOTI2MzI5ODY2.YbMx9A.A5xSi0wKybPhU7wLcC4D1blOWOY
tngn4468z0@dollarnoob.com:qpwo12!@:OTE4ODE3NzgyMjk1MDY0NTc2.YbMx9w.cfaafpNz4IfkLnMH877naiiK_5A
hw7vfau9xw@dollarnoob.com:qpwo12!@:OTE4ODE3NzUxNjY0MDMzODAy.YbMx_A.Kv1DbUrCxMRXhnbT2Y313plNFoI
gi9imvo38y@dollarnoob.com:qpwo12!@:OTE4ODE3ODAwMjQyNDgzMjMw.YbMyBA.OveP5fJiiCXU7cY55eJHrGHFb-c
x06z1oat9d@dollarnoob.com:qpwo12!@:OTE4ODE3ODA4NzczNjk3NTM2.YbMyBg.dvR_yR8lXbnOYLA6oCit_9HnclQ
3o2m7eqlch@dollarnoob.com:qpwo12!@:OTE4ODE3OTI3OTAwMzE1NzM5.YbMyEA.d6PhlRziNQIUuc9Zl9T9MYOwIJY
kcdc1wgxeq@dollarnoob.com:qpwo12!@:OTE4ODE3OTI4MTQ3NzcxNDIz.YbMyGw.L3-TvlU10uimjF4sqAY-THmtOzo
a0xuju8bad@dollarnoob.com:qpwo12!@:OTE4ODE3ODY1MTcwMzA1MDY1.YbMyHA.UTIIY_GJn6WSOTHGejXSE16MW3s
fao304k7nm@dollarnoob.com:qpwo12!@:OTE4ODE3OTAwNDk0NzE2OTY4.YbMyHA.GZ42u30mj37Jl7APPczQeod9J1o
xslkifd223@dollarnoob.com:qpwo12!@:OTE4ODE3OTE2NjkzMTQ3Njg4.YbMyJw.VDm3I7vhCQJn7IfAAoGsgLjbKw8
rh67dxhf79@dollarnoob.com:qpwo12!@:OTE4ODE4MTU1NjYzNjEzOTYy.YbMyRQ._QIiiTxkDy-Cn9i-6_jBZ6dNF6o
7xdechabcw@dollarnoob.com:qpwo12!@:OTE4ODE4MDQzMTM0NjE5Njc5.YbMyRg.bm5uQj8iHVqhv0ZXgsuX2NE2-bA
km4bhg0wg8@dollarnoob.com:qpwo12!@:OTE4ODE4MDM2MjkzNzAxNjQz.YbMySw.tu_Jk33iF2gJk5zICv3I6hmQm4c
pwghdx722x@dollarnoob.com:qpwo12!@:OTE4ODE4MDk0ODk2NTQxNzM2.YbMyTw.yQ6bTC90pT2HYElLk-PktwzP974
7kwj0crqri@dollarnoob.com:qpwo12!@:OTE4ODE4MDM4NjgwMjc2OTky.YbMyUw.5gXo5vOAJNUps5PFgPC5OAOzCLk
bb3jdw8fa1@dollarnoob.com:qpwo12!@:OTE4ODE4MTYxNDk3ODk0OTIy.YbMyXA.roYnFwYB7S3ZMQqzO8jDsNWFThw
'''

result = p.findall(text)
tokens = '\n'.join(result)

print(f'총 찾은 토큰 갯수: {len(result)}개\n[토큰 리스트]\n{tokens}')
