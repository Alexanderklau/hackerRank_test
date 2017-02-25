# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
textwrap.wrap()
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']

textwrap.fill()
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very .....
题目：
输入两个值：
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
输出：
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap
def wrap(string,max_width):
    c = textwrap.fill(string,max_width)
    return c









if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)