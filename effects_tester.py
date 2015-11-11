"""
Name: Cooper Bates
UNI: cbb2153

This file contains main funciton that tests effects.py module
"""
import effects

def main():
    print('\nPortable Pixmap (PPM) Image Editor!\n')
    print('Choose the effect you would like to try\n')
    print('Please enter one effect at a time and press enter\n')
    
    # warns the user that specs must be met for program to work
    print('All files given must be of the same size and exist in directory')
    print('All effects entered must be as numbers between 1 and 6')
    
    print('1) object_filter\n2) shades_of_gray\n3) negate_red')
    print('4) negate_green\n5) negate_blue\n6) mirror\n')
    
    # initializes the effects list to all zeros
    x = [0] * 6
    file_filter_list = []
    
    # asks for and records effects chosen by user as well as file names
    effect_num = int(input('Enter a number: \n')) - 1
    x[effect_num] = 1 
    in_filename = input('Enter an input file name: \n')
    if effect_num == 0:
        more = 'y'
        while more.lower().strip() == 'y':
            add_file = input('Please input your next adittional file: ')
            file_filter_list.append(add_file)
                
            more = input('Do you wish to add another file to filter? y/n')
    out_filename = input('Enter an output file name: \n')
    
    # continues to ask for effects until the user is done
    state = input('Do you wish to choose another effect? y/n')
    while state.lower().strip() == 'y':
        effect_num = int(input('Enter a number: \n')) - 1
        x[effect_num] = 1 
        if effect_num == 0:
            more = 'y'
            while more.lower().strip() == 'y':
                add_file = input('Please input your next adittional file: ')
                file_filter_list.append(add_file)
                
                more = input('Do you wish to add another file to filter? y/n')
    
        state = input('Do you wish to choose another effect? y/n ')
    
    # calls the appy_effects function in effects module, supplying user data
    effects.apply_effects(in_filename, out_filename, x, file_filter_list)
    
    # inicates all effects completed
    print(out_filename, ' created.') 
main()
