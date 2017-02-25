# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
.ljust(width)
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------
.center(width)
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
.rjust(width)
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank

题目：打印标准图形
"""
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone 锥
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars-+
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))








# if __name__ == '__main__':