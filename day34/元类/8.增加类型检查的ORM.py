#!/usr/bin/python3
# author ekubo
# 2023年07月03日
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        # 判断是否要保存
        for k, v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的实例对象
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删除这些已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)
        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name               # 假定数据库表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)  # 通过setattr可以给对象新增属性

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])  # v[0]是元组的第一个元素, 即字段名，v[1]是字段类型
            args.append(getattr(self, k))
        args_temp = list()
        for temp in args:
            # 判断入如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print("sql: %s" % sql)


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u.__dict__)  # 打印的是对象属性
u.save()