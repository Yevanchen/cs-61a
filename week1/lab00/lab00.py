def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """

    # 2020 = 2*1000 + 0*100 + 2*10 + 0*1
    def digits_sum(n):
        s = str(n)
        weights = [10**i for i in range(len(s)-1, -1, -1)]
        return sum(w * digit_at(n, k) for k, w in enumerate(weights, 1))

    return digits_sum(2020)


# 取数字n的第k位（从左到右，1开始），比如 digit_at(2020, 3) == 2
def digit_at(n, k):
    return int(str(n)[k-1])

# int(str(n)[k-1]) 的意思是：
# 1. str(n) 把数字 n 转成字符串，比如 2020 -> "2020"
# 2. [k-1] 取第 k 位（从 0 开始计数），比如 k=3 时就是 "2020"[2]，结果是 "2"
# 3. int(...) 把取出来的字符再转回整数，比如 "2" -> 2


