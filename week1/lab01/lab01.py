
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    #用for 循环生成一个长度为 k的列表 用迭代器从 n开始自减 1的匿名函数用于初始化截断前 k 项 然后用一个循环将其乘起来
    if k == 0:
        return 1
    
    # 生成从n开始自减的k个数字: [n, n-1, n-2, ..., n-k+1]
    numbers = [(lambda i: n - i)(i) for i in range(k)]
    
    # 将所有数字乘起来
    result = 1
    for num in numbers:
        result *= num
    
    return result



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    #step1将数字变成列表项
    list1 = [int(i) for i in str(y)]
    #step2将列表项相加
    return sum(list1)



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"


