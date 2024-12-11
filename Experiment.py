#列表
k=["google",'k',100,10]
print(k[1:3])# 打印1到3左闭右开:   “k,100"
print('\a')#听说\a会有响声
del k[0]  #列表的删除操作
print(k)
k.append('MAKABA')
print(k)
p=k*5
print(p)#*号表示重复，
L=['as','mylover','She']+k
print(L)#+号表示拼接组合，
if 'as' in L:
    print('as in L')
for x in L:
    print(x,end="  ")
###########################################################
###########################################################
#元组
tube=(50)    #无逗号的这样声明会以为是int型
type(tube)

Tube=(50,)   #单个元素有逗号才是元组
types=type(Tube)

#元组无法更改，也无法删除单个元素
#但是可以删除整个元组
del Tube

#元组也和上面一样支持+ += *等操作以及for遍历一级if判断

#将可迭代系列转换为元组。
#tuple(iterable)
T=tuple(k)

#计算元组元素个数。
num=len(T)


###########################################################
###########################################################
#字典
ZiDian={'google':1,
        'nice':2,
        4:3,
        }#使用大括号创建
print('\n')
print(ZiDian[4])
#也可以使用dict
ZiDian2=dict()
ZiDian2['a']=1;
ZiDian2['Teless']="Sheilod";
print(ZiDian2)


###########################################################
###########################################################
#集合——set：无需不重复序列
#可以使用{  }创建也可以使用set()
#但是创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
set1=set(k);
set3=set(["google",2,"look","good","google"])
set2={1,1,2,"apple","banana","nice","banana"}#别看你是这么写的但存储的时候
#就已经自动去重了
print(set1);
print(set2);
print(set3);
#同样适用于in判断
if 'good' in set3:
    print('good in set3')
set4={'abababab'}
print(set4)




