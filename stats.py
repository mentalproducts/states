#! coding: utf-8

from sys import argv
script, path, write_file = argv

from os import listdir
from os.path import isfile
from os.path import join

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
