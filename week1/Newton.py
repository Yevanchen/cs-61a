#这里我们用牛顿法求零点，输入为函数 输出为一个零点 

def newton_method(f, df, initial_guess=1.0, tolerance=1e-10, max_iterations=100):
    """
    使用牛顿法求函数f的零点
    
    参数:
    f: 目标函数
    df: f的导数函数
    initial_guess: 初始猜测值
    tolerance: 精度容忍度
    max_iterations: 最大迭代次数
    
    返回:
    零点的近似值
    """
    x = initial_guess
    for i in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            return x
        
        dfx = df(x)
        if abs(dfx) < tolerance:
            raise ValueError("导数为零，无法继续迭代")
        
        x = x - fx / dfx
    
    raise ValueError("达到最大迭代次数，未找到零点")





