"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes):
    """返回一个按确定性顺序循环遍历 OUTCOMES 的骰子。
    这里的 outcomes 是通过 *args 语法接收的，所以它是一个 tuple，不是 list。
    *outcomes 会将传入的所有参数收集成一个 tuple。
    例如：make_test_dice(1, 2, 3) 中，outcomes = (1, 2, 3)
    如果传入 make_test_dice(3)：
    - outcomes = (3,)，只有一个元素
    - index 初始化为 len(outcomes) - 1 = 0
    - 每次调用 dice()：
      - index = (0 + 1) % 1 = 0
      - 返回 outcomes[0] = 3
    - 所以每次调用都返回 3

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice