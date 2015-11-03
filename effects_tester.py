"""
This file contains main funciton that tests effects.py module
"""
import effects

def main():
    print('\nPortable Pixmap (PPM) Image Editor!\n')
    print('Choose the effect you would like to try:')
    print('1) object_filter\n2) shades_of_gray\n3) negate_red')
    print('4) negate_green\n5) negate_blue\n6) mirror\n')
    effect_num = input('Enter a number: \n')
    in_filename = input('Enter an input file name: \n')
    out_filename = input('Enter an output file name: \n')
    print(out_filename, ' created.') 
    
    x = [0] * 6
    x[effect_num] = 1
    
    effects.apply_effects(in_filename, out_filename, x)

main()