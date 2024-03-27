import shutil
import os

DOWNLOADS = '/Users/azhar/Downloads/'
IMAGES = '/Users/azhar/Downloads/images/'
DOCUMENTS = '/Users/azhar/Downloads/documents/'

image_extensions = {'jpeg':'.jpg','HEIC':'.HEIC','heic':'.heic','PNG':'.png'}
document_extensions = {'pdf':'.pdf', 'txt':'.txt'}

def cleanup(file_path,file_extension):
    #collecting all files based on the type of extension passed within the downloads folder
    files = []
    for f in os.listdir(DOWNLOADS):
        for key, value in file_extension.items():
            #if value in f:
             if f.endswith(value):   
                files.append(f)

    #creating folder based on folder names passed
    for file in files:
        #if file exist
        if os.path.isdir(file_path):
            path = file_path + file
            shutil.move(DOWNLOADS+file,path)
        else:
            #if file does not exist create new file
            os.mkdir(file_path)
            new_path = file_path + file
            shutil.move(DOWNLOADS+file, new_path)


cleanup(IMAGES, image_extensions)
cleanup(DOCUMENTS, document_extensions)






'''
#images = [f for f in os.listdir('/Users/azhar/Downloads') if image_extensions in f.lower()]

images = []
for f in os.listdir('/Users/azhar/Downloads'):
    for key, value in image_extensions.items():
        if value in f:
            images.append(f)

#os.mkdir('/Users/azhar/Downloads/images')

for image in images:
    if os.path.isdir(IMAGES):
        path = IMAGES + image
        shutil.move(DOWNLOADS+image,path)
    else:
        os.mkdir('/Users/azhar/Downloads/images')
        new_path = IMAGES + image
        shutil.move(DOWNLOADS+image, new_path)

def cleanup_images(images):
    for image in images:
        if os.path.isdir(IMAGES):
            path = IMAGES + image
            shutil.move(DOWNLOADS+image,path)
        else:
            os.mkdir('/Users/azhar/Downloads/images')
            new_path = IMAGES + image
            shutil.move(DOWNLOADS+image, new_path)
'''

#Done- creating methods so you can call one method pass in the type of extension and that will execute
#currently i assume if files were named with the extension and the extensions were different - it move wrong files - test this - use lower.endswith('.txt')
#danger-if two files were named the same then it will simply replace - this needs fixing