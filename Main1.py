"""
def capitalize_output(fn):
    def modify(*args, **kwargs):
        x = fn(*args, **kwargs)
        result = x.capitalize()
        print(result)
        return result
    return modify


@capitalize_output
def swap_words(words):
    tmp = words.split(' ')
    return tmp[1] + ' ' + tmp[0]


swap_words("halo bajs")


def double_method(fn):
    def doublex(*args, **kwargs):
        x = fn(*args, **kwargs)
        result = x*2
        print(result)
        return result
    return doublex


@double_method
def mult_on_2(ls):
    result = []
    for x in ls:
        result.append(x * 2)
    return result


mult_on_2([1, 2])


import math


def if_nonpositive(fn):
    def check(x):
        if x < 0:
            print("Нельзя передавать отрицательные числа")
            return -1
        else:
            return fn(x)

    return check


@if_nonpositive
def my_sqrt(x):
    return math.sqrt(x)


print(my_sqrt(-4))


a = list(
    map(lambda x: x+100, [4, 5, 6])
    )

print(a)


x = list(
    filter(lambda x: x%2 == 0, [4, 5, 6])
    )

print(x)

"""

import re


def it_is_correct(something):
    print(re.match("^abc$", something) is not None)
    return re.match("^abc$", something) is not None


def it_is_correct_1(something):
    print(re.match("^a\dc$", something) is not None)
    return re.match("^a\dc$", something) is not None


def it_is_correct_2(something):
    print(re.match("^a\d+c$", something) is not None)
    return re.match("^a\d+c$", something) is not None


def it_is_correct_3(something):
    print(re.match("^a\d*c$", something) is not None)
    return re.match("^a\d*c$", something) is not None


def it_is_correct_4():
    print(re.match("^<a>(.*)</a>$", "<a>halo bajs</a>").groups())
    return re.match("^<a>(.*)</a>$", "<a>halo bajs</a>").groups()
fghfghfghf