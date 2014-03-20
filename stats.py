#! coding: utf-8

from sys import argv
script, path, write_file = argv

from os import listdir
from os.path import isfile
from os.path import join
from copy import deepcopy

data = {}

write_file_o = open(write_file, 'w')


for dir_entry in listdir(path):
    # Opens and reads directory entry if it is a file
    dir_entry_path = join(path, dir_entry)
    if isfile(dir_entry_path):
        with open(dir_entry_path, 'r') as my_file:
            data[dir_entry] = my_file.read()


def count_allfiles(i):
    count = {}

    for x in i:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

    for key in count:
        if count[key] > 0:
            write_file_o.write(key + ':')
            write_file_o.write(str(count[key]) + '\n')


def count_for_each_file(r):
    for each in r:
        write_file_o.write("Statistics in " + str(each))
        count_allfiles(r[each])


def data_split(x):
    for key in x:
        x[key] = x[key].split(' ')
    return x


data_values = data.values()
data_join = ''.join(data_values)
data1_join = deepcopy(data_join)
data_join_words = data1_join.split(' ')
data1 = deepcopy(data)
data_words = data_split(data1)


count_allfiles(data_join)  # Statistics of characters of all files
count_allfiles(data_join_words)  # Statistics of words of all files
count_for_each_file(data)  # Statistics of characters of each file
count_for_each_file(data_words)  # Statistics of words of each file

write_file_o.close()
