#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def calc_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total


ages = [25, 24, 27, 30, 28, 30]
print('Sum of ages: ', calc_sum(ages))


def calc_average(callback, lst):
    average = callback(lst) / len(lst)
    return average


print('The average is: ', calc_average(calc_sum, ages))
ages.sort()
# sort vs sorted
# print(ages.sort())
# print(ages)
copied_ages = sorted(ages, reverse=True)
print(ages)
print(copied_ages)

# Tuples
names_tp = ('James', 'John', 'Jasmine')
print(len(names_tp))
print(names_tp[0])
for name in names_tp:
    print(name)
# Set
empty_varaible = ''
empty_list = []  # list()
empty_dict = {}  # dict()
empty_tuple = ()  # tuple()
companies = {'Facebook', 'Google', 'Apple'}
companies.add('Amazon')
print(companies)
companies.remove('Facebook')
print(companies)
A = {1, 2, 3, 4}
B = {2, 3, 5, 6}
C = A.union(B)  # A U B
D = A.intersection(B)  # A & B
a_with_b = A.difference(B)
print(C)
print(D)
print(a_with_b)
A.clear()
print(A)
del A

file_name = '../datasets/email-exchanges.txt'
file_opened = open(file_name, 'r')
emails = []
for line in file_opened:
    if re.match('[Ff]rom ', line.strip()):
        line = line.strip().split(' ')
        emails.append(line[1])
        print(line)
file_opened.close()
print(emails)

freq_dist = {}
for email in emails:
    if email not in freq_dist:
        freq_dist[email] = 1
    else:
        freq_dist[email] += 1
print(freq_dist)
freq_dist_list = freq_dist.items()
print(freq_dist_list)
keys = freq_dist.keys()
values = freq_dist.values()
print(keys)
print(values)

keys_and_values = sorted(freq_dist_list)
final_freq_table = []
for key, value in keys_and_values:
    final_freq_table.append((value, key))

final_freq_table = sorted(final_freq_table, reverse=True)
print(len(final_freq_table))
print(final_freq_table)
