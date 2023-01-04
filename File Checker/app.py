from pathlib import *

p = Path("\\Users\cbonifacio.FILEBANKINC\Desktop\Test")
p.mkdir()
for file in range(5):
    #q = Path(f"{file}.txt")
    open(f'\\Users\cbonifacio.FILEBANKINC\Desktop\Test\\{file}.txt', 'w')


#with open('readme.txt', 'w') as f:
#    f.write('Create a new text file!')


for file in p.glob('*'):
    print(file)


#Path.rename(target)
