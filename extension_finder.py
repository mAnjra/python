import os

dir_name = os.path.dirname(os.path.abspath(__file__))

count = 0
extensions = set()
for path, sub_dir, files in os.walk(dir_name):
    #if sub_dir:
     #   count = count + len(sub_dir)
    count = count + 1
    if count == 1:
        #print('Root Directory')
        #print('name: ', path) # gives me the path of the direcotry
        #print('\nname: ', sub_dir) # gives me the subdirectories in - there is none in test
        #print('\nname: ', files)
        #print('amount of files', len(files))
        for i in files:
            if '.' in i: # out of bound exception
                #extensions.add(i.split('.',1)[1])
                extensions.add(i.rpartition('.')[-1])
    else:
        continue
        #print('name: ', path) # gives me the path of the direcotry
        #print('\nname: ', sub_dir) # gives me the subdirectories in - there is none in test
        #print('\nname: ', files)
        #print('amount of files', len(files))

print(extensions)
