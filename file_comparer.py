

print('   Welcome to pyFileCompare!')
print('<----------------------------->')

f_selc = input('Please Select the root file: ' '\n'
'\n' 'FILE PATH: ')
f_root = open(f_selc,  'r+')

root_file = f_root.read()
root_file = root_file.lstrip()
root_file = root_file.rstrip()
print('File Char Count: ', len(root_file))
input()

f_comp = input('Please Select the file you want to compare to the root file: ' '\n'
'\n' 'FILE PATH: ')
f_comp_selc = open(f_comp, 'r')

comp_file = f_comp_selc.read()
comp_file = comp_file.lstrip()
comp_file = comp_file.rstrip()
print('File Char Count', len(comp_file))

if root_file == comp_file:
    print('\n''Your Files Match.')
elif root_file != comp_file:
          print('\n' 'Your Files Do Not Match.')


input('\n' 'Press return to exit')
