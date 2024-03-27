import shutil
import os

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
            #if value in f: - below fixes the issue if file is name has an extension in it
             if f.lower().endswith(ext):   
                files.append(f)
                continue
                

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


#Done- creating methods so you can call one method pass in the type of extension and that will execute
#Done- currently i assume if files were named with the extension and the extensions were different - it move wrong files - test this - use lower.endswith('.txt')
#danger-if two files were named the same then it will simply replace - this needs fixing