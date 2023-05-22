# flake8: noqa
import dis
from typing import Any


def f0() -> Any:
    return None
    pass


def f1() -> Any:
    a = 0
    return a
    pass


def f2() -> Any:
    a = 0
    print(a)
    pass


def f3() -> Any:
    a = 0
    a += 1
    print(a)
    pass


def f4() -> Any:
    return range(10)
    pass


def f5() -> Any:
    for i in range(10):
        print(i)
    pass


def f6() -> Any:
    a = 0
    for i in range(10):
        a += 1
    print(a)
    pass


def f8() -> Any:
    x, y = 1, 2
    pass


def f9() -> Any:
    if 1 == 1:
        return 1
    return 2
    pass


def f10() -> Any:
    for i in range(10):
        if i == 3:
            break
    pass


def f11() -> Any:
    list_ = [1, 2, 3]
    dict_ = {'a': 1, 'b': 2}
    return list_, dict_
    pass


def f12() -> Any:
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    return a + b*c/(d**e)
    pass
