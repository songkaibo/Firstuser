def stu(name,age,*args,**kwargs):
    '''
    表示一个学生
    :param name:表示姓名
    :param age:表示年龄
    :param args:表示爱好
    :param kwargs:表示其他
    :return:没有参数
    '''
    pass


print(help(stu))
print("*"*20)
print(stu.__doc__)
