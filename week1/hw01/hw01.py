from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    
    """
    return x*x + y*y + z*z - max(x, y, z)**2
    


def is_factor(n, k):
    """Return True if k is a factor of n."""
    if n % k == 0:
        return True
    else:
        return False

def largest_factor(n):
    """返回小于 n 的最大因子（因数）。

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    for k in range(n-1, 0, -1):
        if is_factor(n, k):
            return k


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    return False

def true_func():
    print(42)


def false_func():
    print(47)


def hailstone(n):
    """打印从 n 开始的冰雹序列并返回其长度。
    
    冰雹序列（Hailstone sequence）也叫考拉兹猜想序列：
    - 如果 n 是偶数，下一个数是 n/2
    - 如果 n 是奇数，下一个数是 3n+1
    - 重复这个过程直到到达 1
    - 序列的长度是从开始到到达 1 的步数

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    step = 0
    current = n
    while(1):   
        if current == 1:
            step += 1
            print(current)
            return step
        if current % 2 == 0:
            next = current//2
            print(current)
        else:
            next = current*3+1
            print(current)
        current = next
        step += 1




