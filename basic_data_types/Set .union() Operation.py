# -*- coding: utf-8 -*-
__author__ = "Yemilice_lau"
"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, 
some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
and the other set is subscribed to the French newspaper. The same student could be in both sets. 
Your task is to find the total number of students who have subscribed to at least one newspaper.
"""
# s =  set("hacker")
# print s.union('rank')
# x = [i for i in range(1,10)]
# print x
# print(input() == 0 or len(set(input().split()).union(input() == 0 or input().split())))
print(len(set(map(int, input().split()))|set(map(int, input().split()))))