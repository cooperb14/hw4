"""
Name: Cooper Bates
UNI: cbb2153

Effects file for assignment 4
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
##############################################################################

def apply_effects(in_filename, out_filename, effects, *filter_filenames):
    '''primary function that is called by the effects_tester. '''

# *filter_filenames stores the names of additional files for the object_filter    
    
    if effects.index(True) == 0:
        pass
    if effects.index(True) == 1:
        shades_of_gray(in_filename, out_filename)
    if effects.index(True) == 2:
        negate_red(in_filename, out_filename)
    if effects.index(True) == 3:
        negate_green(in_filename, out_filename)
    if effects.index(True) == 4:
        negate_blue(in_filename, out_filename)
    if effects.index(True) == 5:
        mirror(in_filename, out_filename)
    else:
        pass    
    
def object_filter(in_file_list, out_file):
    '''Filters out pixel values that appear in only a minority
    of the images in the parameter in_file_list'''
    
    input_file_1 = open(in_file_list[0], "r")
    input_file_2 = open(in_file_list[1], "r")
    input_file_3 = open(in_file_list[2], "r")
    output_file = open(out_file, "w")
    
    lines_1 = input_file_1.readlines()
    lines_2 = input_file_2.readlines()
    lines_3 = input_file_3.readlines()
    header = lines_1[:3]
    
    RGB_1 = convert_pix_to_RGB_list(lines_1)
    RGB_2 = convert_pix_to_RGB_list(lines_2)
    RGB_3 = convert_pix_to_RGB_list(lines_3)
    
    new_pixs = []
    new_pixs = [median(RGB_1, RGB_2, RGB_3, i) for i in range(len(RGB_1))]
    new_pixs = convert_RGB_elements_to_str(new_pixs) +"\n"
    header.append(new_pixs)
    output_file.writelines(header)
    
    input_file_1.close()
    input_file_2.close()
    input_file_3.close()
    output_file.close()
    

def shades_of_gray(in_file, out_file):
    '''Converts the color image in_file to black and white'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    lines = input_file.readlines()
    header = lines[:3]
    RGB_vals = convert_pix_to_RGB_list(lines)
    new_pixs = []
    for i in range(len(RGB_vals)):
        if (i+1)%3 == 0:
            average = (RGB_vals[i] + RGB_vals[i - 1]+ RGB_vals[i - 2])/3
            new_pixs += [average] * 3
    new_pixs = convert_RGB_elements_to_str(new_pixs)
    header.append(new_pixs)
    output_file.writelines(header)
    
    input_file.close()
    output_file.close()

def negate_red(in_file, out_file):
    '''Negates the red in an image'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    lines = input_file.readlines()
    header = lines[:3]
    max_val = int(lines[2].strip('\n'))
    RGB_vals = convert_pix_to_RGB_list(lines)
    new_pixs = []
    for i in range(len(RGB_vals)):
        if i%3 == 0:
            diff = max_val/2 - RGB_vals[i]
            new_pixs.append(round(max_val/2 + diff))
        else:
            new_pixs.append(RGB_vals[i])
    new_pixs = convert_RGB_elements_to_str(new_pixs)
    header.append(new_pixs)
    output_file.writelines(header)

    input_file.close()
    output_file.close()
    
def negate_green(in_file, out_file):
    '''Negates the green in an image'''
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    lines = input_file.readlines()
    header = lines[:3]
    max_val = int(lines[2].strip('\n'))
    RGB_vals = convert_pix_to_RGB_list(lines)
    new_pixs = []
    for i in range(len(RGB_vals)):
        if (i-1)%3 == 0:
            diff = max_val/2 - RGB_vals[i]
            new_pixs.append(round(max_val/2 + diff))
        else:
            new_pixs.append(RGB_vals[i])
    new_pixs = convert_RGB_elements_to_str(new_pixs)
    header.append(new_pixs)
    output_file.writelines(header)

    input_file.close()
    output_file.close()

def negate_blue(in_file, out_file):
    '''Negates the blue in an image'''    
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    lines = input_file.readlines()
    header = lines[:3]
    max_val = int(lines[2].strip('\n'))
    RGB_vals = convert_pix_to_RGB_list(lines)
    new_pixs = []
    for i in range(len(RGB_vals)):
        if (i-2)%3 == 0:
            diff = max_val/2 - RGB_vals[i]
            new_pixs.append(round(max_val/2 + diff))
        else:
            new_pixs.append(RGB_vals[i])
    new_pixs = convert_RGB_elements_to_str(new_pixs)
    header.append(new_pixs)
    output_file.writelines(header)

    input_file.close()
    output_file.close()
    
def mirror(in_file, out_file):
    '''Creates a mirror image by flipping an image horizontally'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    lines = input_file.readlines()
    header = lines[:3]
    adjusted_lines = [i.replace('\n','') for i in lines[3:]]
    result = []
    
    for i in adjusted_lines:
        x = i.split()
        x = [int(i) for i in x]
        package_pixs = [[x[i], x[i+1], x[i+2]] for i in range(0, len(x), 3)]
        package_pixs.reverse()
        concat_pkg = [convert_RGB_elements_to_str(i) for i in package_pixs]
        result.append(' '.join(concat_pkg))
    
    new_lines = ' '.join(result)
    header.append(new_lines)
    output_file.writelines(header)

    input_file.close()
    output_file.close()
    
    
    
    
    
    
    
    
    
    