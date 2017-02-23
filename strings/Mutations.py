# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
替换列表中特定目标的数据
Sample Input
abracadabra
将第5个数据替换成k

Sample Output
abrackdabra
"""

def mutate_string(string, position, character):
    stri = string[:position] + character + string[position + 1:]
    return stri







if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)