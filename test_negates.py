"""
This file is designed to be used for testing all python script
"""

def convert_pix_to_RGB_list(line):
    ls = line.replace('\n', '').split()
    ls = [i.strip(' ') for i in ls]
    ls = [int(i) for i in ls]
    return ls

def convert_RGB_elements_to_str(ls):
    return ' ' .join([str(i) for i in ls])
    
    
entered = ["tetons1new.ppm", "tetons2new.ppm", "tetons3new.ppm"]
######################################################################
#open files

import linecache

file_1 = open(entered[0], "r")
temp = open('temp.ppm', "w")


max_val = int(linecache.getline(entered[0], 3).strip(' '))

counter = 0
for n in file_1:
    if counter < 3:
        temp.write(n)
        counter += 1
    else:
        ls = convert_pix_to_RGB_list(n)
        for i in range(len(ls)):
            if (i-2)%3 == 0:
                ls[i] = (max_val - ls[i])
        temp.write(convert_RGB_elements_to_str(ls) + ' ')


#for i in range(len(pixs_1)):
#    if i%3 == 0:
#        average = (pixs_1[i] + pixs_1[i - 1]+ pixs_1[i - 2])/3
#        good_pixs += [average] * 3

file_1.close()
temp.close()

