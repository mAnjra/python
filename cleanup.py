import shutil
import os

'''
Download folder cleaner - dumps files into folder
'''

DOWNLOADS = '/Users/azhar/Downloads/'
IMAGES = '/Users/azhar/Downloads/images/'
DOCUMENTS = '/Users/azhar/Downloads/documents/'

image_extensions = {'.jpg','.HEIC','.heic','.png'}
document_extensions = {'.pdf', '.txt'}

def cleanup(file_path,file_extension):
    #collecting all files based on the type of extension passed within the downloads folder
    files = []
    for f in os.listdir(DOWNLOADS):
        for ext in file_extension:
            #if value in f: - below fixes the issue if file name has an extension in it
             if f.lower().endswith(ext):   
                files.append(f)
                continue
                
    #creating folder based on folder names passed
    for file in files:
        #make new directory if folder does not exists else move on
        os.makedirs(file_path, exist_ok=True)
        path = file_path + file
        # check if file already exists in new folder and then dont copy it over
        if not os.path.exists(path):
            shutil.move(DOWNLOADS+file, path)
       
cleanup(IMAGES, image_extensions)
cleanup(DOCUMENTS, document_extensions)


#Done- creating methods so you can call one method pass in the type of extension and that will execute
#Done- currently i assume if files were named with the extension and the extensions were different - it move wrong files - test this - use lower.endswith('.txt')
#danger-if two files were named the same then it will simply replace - this needs fixing - not actually fixed, temp solution to not copy