# -*- coding: utf-8 -*-

def create_class_by_type():
    '''
    这里只是说简单从原理上说明了两种方式就结果而言别无二致。
    但是由于一般都是__init__来进行类的初始化,第二种方式怎么完成这点呢？(属性字典中的`__init__`指向可引用的一个函数),
    类当中的特殊命名方法协议并没有发生什么变化
    '''
    class CreateClassNormalWay(object):
        attr = 'a'
    CreateClassByType = type('CreateClassByType', (object, ), dict(attr='a'))

    assert CreateClassNormalWay.__class__ == CreateClassByType.__class__
    assert dir(CreateClassNormalWay) == dir(CreateClassByType)
    assert CreateClassNormalWay.__base__ == CreateClassByType.__base__

    class CreateClassNormalWay2(object):
        def __init__(self, name):
            self.name = name

    def init(cls, name):
        cls.name = name
    CreateClassByType2 = type('CreateClassByType2', (object, ), dict(__init__=init))

    normal_way = CreateClassNormalWay2('nw')
    by_type = CreateClassByType2('bt')
    assert CreateClassNormalWay2.__class__ == CreateClassByType2.__class__
    assert dir(CreateClassNormalWay2) == dir(CreateClassByType2)
    assert dir(normal_way) == dir(by_type)
    assert normal_way.name == 'nw'
    assert by_type.name == 'bt'

def use_metaclass_by_attribute():
    # @metaclass
    def capitalize_attrs(class_name, class_parents, class_attrs):
        capitalize_attrs = dict( (name.capitalize(), attr) for name,attr in class_attrs.iteritems()\
                                 if not name.startswith('_'))
        return type(class_name, class_parents, capitalize_attrs)
    # __metaclass__ = capitalize_attrs 作用域不限于类声明中
    class Test(object):
        __metaclass__ = capitalize_attrs
        at = 'at_test'
        def __init__(self, name):
            self.name = name

    assert not hasattr(Test,'at')
    assert hasattr(Test, 'At')
    assert not hasattr(Test, 'Name')
    assert not hasattr(Test, 'name')
    t = Test('a') #object() takes no parameters... @todo
    assert not hasattr(t, 'name')
    assert hasattr(t, 'Name')

def use_metaclass_by_new():
    '''
    在type创建类之前做一些手脚
    @metaclass
    '''
    class CapitalizeMetaClass(type):
        at = 'at_test'
        def __new__(capitalize_metaclass, class_name, class_parents, class_attrs):
            capitalize_attrs = dict( (name.capitalize(), attr) for name,attr in class_attrs.iteritems()\
                                     if not name.startswith('_'))
            return type(class_name, class_parents, capitalize_attrs)
            #OOP style
            # return type.__new__(capitalize_metaclass, class_name, class_parents, capitalize_attrs)
    cm = CapitalizeMetaClass('CM', (object, ), dict(at='a'))
    assert hasattr(cm, 'At')

if __name__ == '__main__':
#    use_metaclass_by_attribute()
#    create_class_by_type()
    use_metaclass_by_new()