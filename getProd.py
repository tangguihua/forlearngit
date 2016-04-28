from functools import reduce
def prod(L):
    def mul(x,y):
        return x*y
    return reduce(mul,L)

#def _isnum():
        
def is_palindrome(n):
    num = n
    n1 = 0
    while num != 0:
        m = num % 10
        n1 = n1 * 10 + m
        num = num // 10

    return n1 == n
#@log    
def now():
    print('2016-4-28')
    
def log(func):
    def wrapper(*args, **kw):
        print('call %s():'%func.__name__)
        return func(*args, **kw)
    return wrapper