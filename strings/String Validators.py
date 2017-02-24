# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
str.isalnum():判断str中含有的(a-z, A-Z and 0-9)，如果存在其他，输出false.
str.isalpha():判断str中含有的(a-z and A-Z).如果存在其他，输出false.
str.isdigit():判断str中含有的 (0-9).如果存在其他，输出false.
str.islower():判断str中含有的 (a-z).如果存在其他，输出false.
str.isupper():判断str中含有的(A-Z).如果存在其他，输出false.
# 题目：
输入一个值，上述五种方法分别判断
"""
if __name__ == '__main__':
    S = input()
    print("True" if len([s for s in S if s.isalnum()]) > 0 else "False")
    #如果s在S中，并且s.isalnum判定为真。输出True，否则输出False
    print("True" if len([s for s in S if s.isalpha()]) > 0 else "False")
    print("True" if len([s for s in S if s.isdigit()]) > 0 else "False")
    print("True" if len([s for s in S if s.islower()]) > 0 else "False")
    print("True" if len([s for s in S if s.isupper()]) > 0 else "False")