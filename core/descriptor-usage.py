# -*- coding: utf-8 -*-

def reallife_descriptor():
    # @descriptor @装饰器    
    from werkzeug._internal import _missing
    
    class cached_property(object):
        # @werkzeug.utils class:cached_property
        # 开源协议,版权详见:https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/utils.py
        """A decorator that converts a function into a lazy property. The
        function wrapped is called the first time to retrieve the result
        and then that calculated result is used the next time you access
        the value::
        
        class Foo(object):
    
            @cached_property
            def foo(self):
                # calculate something important here
                return 42
        The class has to have a `__dict__` in order for this property to
        work.
        """
        # implementation detail: this property is implemented as non-data
        # descriptor. non-data descriptors are only invoked if there is
        # no entry with the same name in the instance's __dict__.
        # this allows us to completely get rid of the access function call
        # overhead. If one choses to invoke __get__ by hand the property
        # will still work as expected because the lookup logic is replicated
        # in __get__ for manual invocation.    
        def __init__(self, func, name=None, doc=None):
            self.__name__ = name or func.__name__
            self.__module__ = func.__module__
            self.__doc__ = doc or func.__doc__
            self.func = func
        def __get__(self, obj, type=None):
            if obj is None:
                return self
            value = obj.__dict__.get(self.__name__, _missing)
            if value is _missing:
                value = self.func(obj)
                obj.__dict__[self.__name__] = value
            return value

def descriptor_use():
    # @descriptor @装饰器
    class CacheProperty(object):
        _cached_value = ''
        def __get__(self, instance, klass):
            return self._cached_value
        def __set__(self, instance, value):
            self._cached_value = value
    class User(object):
        name = CacheProperty()
    assert hasattr(User, 'name')
    u = User()
    print User.__dict__
    assert hasattr(u, 'name')
    assert u.__dict__ == dict() # 空,但是上面显示实例是有属性.
    u.name = 'acd'
    assert u.name == 'acd'
    assert u.__dict__ == dict() # 仍然为空
    # 实际发生了:
    assert u.name is User.__dict__['name'].__get__(u, User)
if __name__ == '__main__':
    descriptor_use()