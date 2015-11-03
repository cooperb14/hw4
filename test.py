"""
This file is designed to be used for testing all python script
"""
def convert_pix_to_RGB_list(line):
    pix_str = " ".join(line[3:]).replace('\n', '').split()[3:]
    RGB_lst = [int(i) for i in pix_str]
    return RGB_lst

def convert_RGB_elements_to_str(ls):
    return ' ' .join([str(i) for i in ls])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


file_1 = open("tetons1new.ppm", "r")
file_2 = open("tetons2new.ppm", "r")
file_3 = open("tetons3new.ppm", "r")
temp = open('temp.ppm', "w")


pixs_1 = file_1.readlines()
pixs_2 = file_2.readlines()
pixs_3 = file_3.readlines()

header = pixs_1[:3]
result = []

lines = [i.replace('\n','') for i in pixs_1[3:]]
for i in lines:
    x = i.split()
    x = [int(i) for i in x]
    package_pixs = [[x[i], x[i+1], x[i+2]] for i in range(0, len(x), 3)]
    package_pixs.reverse()
    y = [convert_RGB_elements_to_str(i) for i in package_pixs]
    result.append(' '.join(y))
    
lines = ' '.join(result)
header.append(lines)


temp.writelines(header)






file_1.close()
file_2.close()
file_3.close()
temp.close()