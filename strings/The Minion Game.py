# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
题目：输入两个，判断它有多少种组合方法，并且输出。
input:banana  anana

"""

s = input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print ("Kevin", kevsc)
elif kevsc < stusc:
    print ("Stuart", stusc)
else:
    print ("Draw")







# if __name__ == '__main__':