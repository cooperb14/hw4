"""
This file is designed to be used for testing all python script
"""
import linecache

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
entered = ["tetons1new.ppm", "tetons2new.ppm", "tetons3new.ppm"]

file_1 = open(entered[0], "r")
temp = open('temp.ppm', "w")

i = 1
for n in file_1:
    if i <= 3:
        temp.write(linecache.getline(entered[1], i))
    else:
        ls_1 = convert_pix_to_RGB_list(linecache.getline(entered[0], i))
        ls_2 = convert_pix_to_RGB_list(linecache.getline(entered[1], i))
        ls_3 = convert_pix_to_RGB_list(linecache.getline(entered[2], i))
        new_pixs = []
        new_pixs = [median(ls_1, ls_2, ls_3, x) for x in range(len(ls_1))]
        temp.write(convert_RGB_elements_to_str(new_pixs) + '\n')
    i += 1

file_1.close()
temp.close()