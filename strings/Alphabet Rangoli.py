# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
输入：5
输出：
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * size -3,"-"))
    print('\n'.join(L[:0:-1] + L))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)