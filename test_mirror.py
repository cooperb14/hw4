"""
Trying to mirror
"""
def convert_pix_to_RGB_list(line):
    ls = line.replace('\n', '').split()
    ls = [i.strip(' ') for i in ls]
    ls = [int(i) for i in ls]
    return ls

def convert_RGB_elements_to_str(ls):
    return ' ' .join([str(i) for i in ls])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


file_1 = open("tetons1new.ppm", "r")
temp = open('temp.ppm', "w")


counter = 0
for n in file_1:
    if counter < 3:
        temp.write(n)
        counter += 1
    else:
        ls  = convert_pix_to_RGB_list(n)
        pkg_pixs = [[ls[i], ls[i+1], ls[i+2]] for i in range(0, len(ls), 3)]
        pkg_pixs.reverse()
        line = ' '.join([convert_RGB_elements_to_str(i) for i in pkg_pixs])
        
        temp.write(line + ' ')

file_1.close()
temp.close()