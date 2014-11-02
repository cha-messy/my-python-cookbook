# -*- coding: utf-8 -*-

from functools import wraps

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

def wrap_coroutine_decorator():
    def coroutine_with_wrap(func):
        @wraps(func)
        def start(*args, **kwargs):
            '''
            start doc
            '''
            cr = func(*args, **kwargs)
            next(cr)
            return cr
        return start
    
    @coroutine_with_wrap
    def countdown_with_wrap(n):
        '''
        countdown doc
        '''
        while n > 0:
            yield n
            n -= 1

    print countdown_with_wrap.__doc__ # output: countdown doc
    print countdown_with_wrap.__name__ # output: countdown_with_wrap



