Name: Cooper Bates
UNI: cbb2153



HW4 Image Editor

Description:
The apply_effects function inside the effects module is the master function controlling all of the 6 effects functions. Getting user data inputed through the effects_tester module, apply_effects passes filenames in as arguments to the various effects, opens them inside each effect, modifies them, closes them, and assigns their output name to a temporary variable “transition_file” to allow for consecutive effects to be applied. Each effect is extremely similar in that it performs modifications on the the input file in the following steps:
1)read the file line by line
2)convert each line from a string to a list of RGB values
3)manipulate RGB values mathematically to execute effect assigned
4)convert list of RGB values back to a string with end_line marker
5)write string line by line to output file

Multiple effects are able to be applied and for the object_filer effect, as many files as the user wishes to filter may be inputed and executed. In addition, several helper functions exist at the top of the effects module to aid in the mathematical manipulation of RGB values and string/list conversion

For the object_tester, the user is prompted to enter values specific to the effects available, as well as to not enter invalid information such as incompatible file sizes, or file names that do not exist in the directory. The effects chosen by the user, as well as the several file names are passed as arguments to the effects.appy_effects function

Bugs:
No bugs that I a currently aware of. The program will crash if user inputs data not to the specifications CLEARLY written in the displayed directions.

Additional Comments:
Multiple effects method passes file name as method, not file object, which is less efficient but still effective and within reason.
