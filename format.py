#1.通过位置
print('i am {0},i am {1}'.format('leo',23))
#2.通过关键字参数
print('i am {name},i am {age}'.format(name='leo',age=23))
#3.通过对象属性来判断
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
leo=person('leo',23)
print('i am {self.name},i am {self.age}'.format(self=leo))
# 通过下标
print('{0[0]}{0[1]}{1[0]}{1[1]}'.format(['i am ','leo'],[',i am ',23]))
# 精度与类型f
print('{:.2f}'.format(123.456789))
# b、d、o、x分别是二进制、十进制、八进制、十六进制。
print('{:b}'.format(17))
print('{:d}'.format(17))
print('{:o}'.format(17))
print('{:x}'.format(17))
# 号还能用来做金额的千位分隔符。
print('{:,}'.format(123456789))