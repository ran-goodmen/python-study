#!/usr/bin/python3
# author ekubo
# 2023年07月03日
"""
模拟django里的ORM编写类，例：若我们要新增模型类User，只需继承Model类，然后写字段和字段类型即可
"""


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, tuple):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return super().__new__(cls, name, bases, attrs)  # 官方写法是super()而不是type


class Model(metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        args_temp = list()
        for temp in args:
            # 判断入如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL: %s' % sql)


class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u.__dict__)
u.save()
