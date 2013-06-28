#-------------------------------------------------------------------------------
# Name:        pyfileComparer
# Purpose:     Compare text files to see if they are different.
# Author:      Zach Tuttle
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

print('   Welcome to pyFileCompare!')
print('<----------------------------->')

f_selc = raw_input('Please Select the root file: ' '\n'
'\n' 'FILE PATH: ')
f_root = open(f_selc,  'r+')

root_file = f_root.read()
root_file = root_file.lstrip()
root_file = root_file.rstrip()
print("File Char Count:", len(root_file))
raw_input('\n' 'Press return to continue...' '\n')

f_comp = raw_input('Please Select the file you want to compare to the root file: ' '\n'
'\n' 'FILE PATH: ')
f_comp_selc = open(f_comp, 'r')

comp_file = f_comp_selc.read()
comp_file = comp_file.lstrip()
comp_file = comp_file.rstrip()
print('\n' 'File Char Count:', len(comp_file))

if root_file == comp_file:
    print('\n''Your Files Match.')
elif root_file != comp_file:
          print('\n' 'Your Files Do Not Match.')


raw_input('\n' 'Press return to exit')
