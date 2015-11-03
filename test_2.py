"""
This file is designed to be used for testing all python script
"""

def convert_pix_to_RGB_list(line):
    pix_str = " ".join(line[3:]).replace('\n', '').split()[3:]
    RGB_lst = [int(i) for i in pix_str]
    return RGB_lst

def convert_RGB_elements_to_str(ls):
    return ' ' .join([str(i) for i in ls])
    
def median(ls_1, ls_2, ls_3, count):
    ls_comp = [ls_1[count], ls_2[count], ls_3[count]]
    return sorted(ls_comp)[len(ls_comp)//2]
    
entered = ["tetons1new.ppm", "tetons2new.ppm", "tetons3new.ppm"]

#open files
file_1 = open(entered[0], "r")
file_2 = open(entered[1], "r")
file_3 = open(entered[2], "r")
temp = open('temp.ppm', "w")

lines_1 = file_1.readlines()
lines_2 = file_2.readlines()
lines_3 = file_3.readlines()

header = lines_1[:3]
max_val = int(lines_1[2].strip('\n'))


pixs_1 = convert_pix_to_RGB_list(lines_1)
pixs_2 = convert_pix_to_RGB_list(lines_2)
pixs_3 = convert_pix_to_RGB_list(lines_3)

good_pixs = []
#for i in range(len(pixs_1)):
#    if i%3 == 0:
#        average = (pixs_1[i] + pixs_1[i - 1]+ pixs_1[i - 2])/3
#        good_pixs += [average] * 3
for i in range(len(pixs_1)):
        if i%3 == 0:
            diff = max_val/2 - pixs_1[i]
            good_pixs.append(round(max_val/2 + diff))
        else:
            good_pixs.append(pixs_1[i])
        
#good_pixs = [median(pixs_1, pixs_2, pixs_3, i) for i in range(len(pixs_1))]
good_pixs = convert_RGB_elements_to_str(good_pixs) +"\n"

header.append(good_pixs)
temp.writelines(header)


file_1.close()
file_2.close()
file_3.close()
temp.close()

