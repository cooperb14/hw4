"""
Name: Cooper Bates
UNI: cbb2153

Effects file for assignment 4
"""

import linecache
import statistics
import os


def convert_pix_to_RGB_list(line):
    '''converts file line to list of RGB vals'''
    
    ls = line.replace('\n', '').split()
    ls = [i.strip(' ') for i in ls]
    ls = [int(i) for i in ls]
    return ls


def convert_RGB_elements_to_str(ls):
    '''converts integer list of RGB vals to a string'''
    
    return ' ' .join([str(i) for i in ls]) 
    
    
def mode(RGB_list, count):
    ''' Gets mode element of a list given'''
    
    temp = []
    for index in RGB_list:
        temp.append(index[count])
    return statistics.mode(temp)
    
    
def remove(file_name):
    '''removes a given file from directory'''
    
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass
    
##############################################################################

def apply_effects(in_filename, out_filename, effects, *filter_filenames):
    '''primary function that is called by the effects_tester. '''
    
# *filter_filenames stores the names of additional files for the object_filted

    transition_file = in_filename
    
# applies effects based on user input. Adjusts filenames for mult. effects
    if effects[0]:
        in_files = []
        in_files.append(in_filename)
        
        # Tailors in_files in the case that filter_filenames is list 
        for entries in filter_filenames:
            if type(entries) is list:
                for name in entries:
                    in_files.append(name)
            else:
                in_files.append(entries)
                
        object_filter(in_files, 'filter.ppm')
        transition_file = 'filter.ppm'
    if effects[1]:
        shades_of_gray(transition_file, 'grey_shades.ppm')
        transition_file = 'grey_shades.ppm'
    if effects[2]:
        negate_red(transition_file, 'red_negate.ppm')
        transition_file = 'red_negate.ppm'
    if effects[3]:
        negate_green(transition_file, 'green_negate.ppm')
        transition_file = 'green_negate.ppm'
    if effects[4]:
        negate_blue(transition_file, 'blue_negate.ppm')
        transition_file = 'blue_negate.ppm'
    if effects[5]:
        mirror(transition_file, 'mirror.ppm')
        transition_file = 'mirror.ppm'
   
# renames final output file to user's request
    os.rename(transition_file, out_filename)
    
# deletes all unncecssary temp files created during mult. effects
    if effects[0]:
        remove('filter.ppm')
    if effects[1]:
        remove('grey_shades.ppm')
    if effects[2]:
        remove('red_negate.ppm')
    if effects[3]:
        remove('green_negate.ppm')
    if effects[4]:
        remove('blue_negate.ppm')
    if effects[5]:
        remove('mirror.ppm')
    
    
def object_filter(in_files, out_file):
    '''Filters out pixel values that appear in only a minority
    of the images in the parameter in_file_list'''
    
    input_file_1 = open(in_files[0], "r")
    output_file = open(out_file, "w")
    
    # reads input files line by line, modifies RGB values, and writes output
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
    
    input_file_1.close()
    output_file.close()
    

def shades_of_gray(in_file, out_file):
    '''Converts the color image in_file to black and white'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    # reads input files line by line, modifies RGB values, and writes output
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
        output_file.write(convert_RGB_elements_to_str(new_pixs) + '\n')
    
    input_file.close()
    output_file.close()

def negate_red(in_file, out_file):
    '''Negates the red in an image'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    # sets max RGB value based on file header
    max_val = int(linecache.getline(in_file, 3).strip(' '))
    
    # reads input files line by line, modifies RGB values, and writes output
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
            output_file.write(convert_RGB_elements_to_str(ls) + '\n')

    input_file.close()
    output_file.close()
    
def negate_green(in_file, out_file):
    '''Negates the green in an image'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    # sets max RGB value based on file header
    max_val = int(linecache.getline(in_file, 3).strip(' '))
    
    # reads input files line by line, modifies RGB values, and writes output
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
            output_file.write(convert_RGB_elements_to_str(ls) + '\n')
            
    input_file.close()
    output_file.close()

def negate_blue(in_file, out_file):
    '''Negates the blue in an image'''    
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    # sets max RGB value based on file header
    max_val = int(linecache.getline(in_file, 3).strip(' '))
    
    # reads input files line by line, modifies RGB values, and writes output
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
            output_file.write(convert_RGB_elements_to_str(ls) + '\n')
            
    input_file.close()
    output_file.close()
    
def mirror(in_file, out_file):
    '''Creates a mirror image by flipping an image horizontally'''
    
    input_file = open(in_file, "r")
    output_file = open(out_file, "w")
    
    # reads input files line by line, modifies RGB values, and writes output
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
            output_file.write(line + '\n')

    input_file.close()
    output_file.close()
    
    
    
    
    
    
    
    
    
    