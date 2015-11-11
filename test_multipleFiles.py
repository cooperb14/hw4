# -*- coding: utf-8 -*-
"""
testing multiple effects
"""
import linecache
import statistics

def convert_pix_to_RGB_list(line):
    ls = line.replace('\n', '').split()
    ls = [i.strip(' ') for i in ls]
    ls = [int(i) for i in ls]
    return ls

def convert_RGB_elements_to_str(ls):
    return ' ' .join([str(i) for i in ls])
    
def median(ls_1, ls_2, ls_3, count):
    ls_comp = [ls_1[count], ls_2[count], ls_3[count]]
    return sorted(ls_comp)[len(ls_comp)//2]
    
def mode(RGB_list, count):
    temp = []
    for index in RGB_list:
        temp.append(index[count])
    return statistics.mode(temp)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


in_files = ['tetons1new.ppm', 'tetons2new.ppm', 'tetons3new.ppm', 'tetons_copy.ppm', 'tetons_copy2.ppm']
out_file = 'temp.ppm'

input_file_1 = open(in_files[0], "r")
output_file = open('temp.ppm', "w")

i = 1
for n in input_file_1:
    if i <= 3:
        output_file.write(linecache.getline(in_files[0], i))
    else:
        ls = []
        for files in in_files:
            line = linecache.getline(files, i)
            ls.append(convert_pix_to_RGB_list(line))
        new_pixs = []
        for x in range(len(ls[0])):
            new_pixs.append(mode(ls, x))
        output_file.write(convert_RGB_elements_to_str(new_pixs) + '\n')
    i += 1         

#in_file = open(in_files[1], 'r')
#count = 0
#for n in in_file:
#    count += 1
#print(count)
#in_file.close()
input_file_1.close()
output_file.close()

