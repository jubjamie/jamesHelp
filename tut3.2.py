# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:37:09 2020

@author: james
"""


f = open("data1.txt", "r")
print(f.read())


def read_data(filename):
    infile = open(filename, 'r')
    my_data = []
    for line in infile:
        number = float(line)
        my_data.append(number)
    infile.close()
    return my_data


print(read_data("data1.txt"))


def fileaverage(data):
    if len(data) < 1:
        return None
    mysum = 0.0
    for item in data:
        mysum += item
    average = mysum / len(data)
    return [average, data]

t = fileaverage(read_data("data1.txt"))[1][-3:-1]

print(t)

print(fileaverage(read_data("data1.txt")))
