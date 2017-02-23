# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
Sample Input
this is a string

Sample Output
this-is-a-string
"""
def split_and_join(line):
    c = line.split()
    return  "-".join(c)
    # return line.split() and "-".join(line)







if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)