def improve(update, close, guess=1):
        while not close(guess):
            guess = update(guess)
        return guess

#彻底理解improve方法，主要是将传入一个更新函数 以及一个评估函数，还有一个起点 意味将这个起点交给更新函数每一轮以评估函数作为退出条件

'''
>>> def golden_update(guess):
        return 1/guess + 1

>>> def square_close_to_successor(guess):
        # approx_eq(a, b) 检查 a 和 b 是否“近似相等”，通常用于浮点数比较，避免精度误差。
        # 这里 approx_eq(guess * guess, guess + 1) 判断 guess^2 是否接近 guess+1。
        # 这是黄金比例的定义方程 φ^2 = φ + 1。
        return approx_eq(guess * guess, guess + 1)
def approx_eq(a, b, tol=1e-15):
    return abs(a - b) < tol

'''

#解决问题  计算一个数的平方根。在编程语言中，“平方根”通常缩写为 sqrt。重复应用以下更新，值会收敛为 a 的平方根，比如求 3的配方根，那我们的目标相当于用更新函数来实现一个求根

def average(x, y):
        return (x + y)/2

def sqrt_update(x, a):
        return average(x, a/x)

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tol=1e-5):
    # 1e-5 就是 0.00001，表示允许的最大误差（精度），
    # 只要 x 和 y 的差小于 0.00001 就认为“足够接近”
    return abs(x - y) < tol

def sqrt(a):
    def average(x, y):
        return (x + y)/2

    def sqrt_update(x):
        return average(x, a/x)
    
    def sqrt_close(x):
        return approx_eq(x*x,a)
    
    def improve(update, close, guess=1):
        round = 1
        while not close(guess):
            orgin = guess
            guess = update(guess)
            round = round+1
            print(f"这是第 {round} 次。我被从{orgin}更新到了{guess}")
        return guess
    
    return improve(sqrt_update,sqrt_close,a)

x=sqrt(256)
print(x)