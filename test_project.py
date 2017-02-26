# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
# def print_formatted(number):
#     width = len("{0:b}".format(number))
#     for i in range(1, n + 1):
#         # print("{0:{width}d}".format(i,width=width))
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
#
#     # your code goes here
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
import string
a = string.ascii_lowercase
#小写字母
# b = int(input())
# L = []
# for i in range(b):
#     s = "-".join(a[i:b])
#     L.append(s[::-1] + s[1:]).center()
# #center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格
# print(L)
#     # print(s)
# # print(a)

s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)






# if __name__ == '__main__':