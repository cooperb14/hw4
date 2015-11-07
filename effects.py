"""
Name: Cooper Bates
UNI: cbb2153

Effects file for assignment 4
"""
import linecache

def convert_pix_to_RGB_list(line):
    ls = line.replace('\n', '').split()
    ls = [i.strip(' ') for i in ls]
    ls = [int(i) for i in ls]
    return ls

def convert_RGB_elements_to_str(ls):
    return ' ' .join([str(i) for i in ls]) 
# this will have to change to a 'mode' function when using > 3 files
def median(ls_1, ls_2, ls_3, count):
    ls_comp = [ls_1[count], ls_2[count], ls_3[count]]
    return sorted(ls_comp)[len(ls_comp)//2]
##############################################################################

def apply_effects(in_filename, out_filename, effects, *filter_filenames):
    '''primary function that is called by the effects_tester. '''

# *filter_filenames stores the names of additional files for the object_filted
    
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
    
def object_filter(in_files, out_file):
    '''Filters out pixel values that appear in only a minority
    of the images in the parameter in_file_list'''
    
    input_file_1 = open(in_files[0], "r")
    output_file = open(out_file, "w")
    
    i = 1
    for n in input_file_1:
        if i <= 3:
            output_file.write(linecache.getline(in_files[0], i))
        else:
            ls_1 = convert_pix_to_RGB_list(linecache.getline(in_files[0], i))
            ls_2 = convert_pix_to_RGB_list(linecache.getline(in_files[1], i))
            ls_3 = convert_pix_to_RGB_list(linecache.getline(in_files[2], i))
            
            new_pixs = []
            new_pixs = [median(ls_1, ls_2, ls_3, x) for x in range(len(ls_1))]
            output_file.write(convert_RGB_elements_to_str(new_pixs) + ' ')
        i += 1         
    
    input_file_1.close()
    output_file.close()
    

def shades_of_gray(in_file, out_file):
    '''Converts the color image in_file to black and white'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    new_pixs = []
    counter = 0
    for n in input_file:
        if counter < 3:
            output_file.write(n)
            counter += 1
        else:
            ls = convert_pix_to_RGB_list(n)
            new_pixs = []
            for i in range(0, len(ls), 3):
                average = (ls[i] + ls[i + 1] + ls[i + 2])/3
                new_pixs.extend([average] * 3)
        output_file.write(convert_RGB_elements_to_str(new_pixs) + ' ')
    
    input_file.close()
    output_file.close()

def negate_red(in_file, out_file):
    '''Negates the red in an image'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    max_val = int(linecache.getline(in_file, 3).strip(' '))

    counter = 0
    for n in input_file:
        if counter < 3:
            output_file.write(n)
            counter += 1
        else:
            ls = convert_pix_to_RGB_list(n)
            for i in range(len(ls)):
                if i%3 == 0:
                    ls[i] = (max_val - ls[i])
            output_file.write(convert_RGB_elements_to_str(ls) + ' ')

    input_file.close()
    output_file.close()
    
def negate_green(in_file, out_file):
    '''Negates the green in an image'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    max_val = int(linecache.getline(in_file, 3).strip(' '))

    counter = 0
    for n in input_file:
        if counter < 3:
            output_file.write(n)
            counter += 1
        else:
            ls = convert_pix_to_RGB_list(n)
            for i in range(len(ls)):
                if (i-1)%3 == 0:
                    ls[i] = (max_val - ls[i])
            output_file.write(convert_RGB_elements_to_str(ls) + ' ')
            
    input_file.close()
    output_file.close()

def negate_blue(in_file, out_file):
    '''Negates the blue in an image'''    
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    max_val = int(linecache.getline(in_file, 3).strip(' '))

    counter = 0
    for n in input_file:
        if counter < 3:
            output_file.write(n)
            counter += 1
        else:
            ls = convert_pix_to_RGB_list(n)
            for i in range(len(ls)):
                if (i-2)%3 == 0:
                    ls[i] = (max_val - ls[i])
            output_file.write(convert_RGB_elements_to_str(ls) + ' ')
            
    input_file.close()
    output_file.close()
    
def mirror(in_file, out_file):
    '''Creates a mirror image by flipping an image horizontally'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    counter = 0
    for n in input_file:
        if counter < 3:
            output_file.write(n)
            counter += 1
        else:
            ls  = convert_pix_to_RGB_list(n)
            pkg = [[ls[i], ls[i+1], ls[i+2]] for i in range(0, len(ls), 3)]
            pkg.reverse()
            line = ' '.join([convert_RGB_elements_to_str(i) for i in pkg])
            output_file.write(line + ' ')

    input_file.close()
    output_file.close()
    
    
    
    
    
    
    
    
    
    