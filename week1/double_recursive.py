# def is_even(n):
#     if n == 0:
#         return True
#     else:
#         return is_odd(n-1)
# def is_odd(n):
#     if n == 0:
#         return False
#     else :
#         return is_even(n-1)


def is_even(n):
    if n==0:
        return True
    else:
        return is_odd(n-1)

print(is_even(10))
print(is_even(11))


def is_odd(n):  # 奇数
    if n==0:
        return False
    else:
        return is_even(n-1)
    
print(is_odd(10))
print(is_odd(11))
    
#让我们将is_even和is_odd函数结合起来，实现一个函数，判断一个数是否是偶数

def is_even(n):
    if n==0:
        return True
    else:
        if n-1==0:
            return False
        else:
            return is_even((n-1)-1)
        

            

    
    




def is_odd(n):
    if n==0:
        return False
    else:
        return is_even(n-1)
    

#如果一个数比一个奇数大 1，那它就是偶数
#如果一个数比一个偶数大 1，那它就是奇数