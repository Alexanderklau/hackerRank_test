# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
Sample Input
hello world


Sample Output
Hello World
"""
def capitalize(string):
    for x in string[:].split():
        string = string.replace(x, x.capitalize())
    return string
    # return string.title()
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)









# if __name__ == '__main__':