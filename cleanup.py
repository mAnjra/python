import shutil
import os
import random
import time
import logging

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

'''
Download folder cleaner - dumps files into folder
'''
random.seed()

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
        else:
            #rename file and then move over to images
            file_rename = f'(Copy ID: {random.random()}) {file}'
            os.rename(DOWNLOADS+file, DOWNLOADS+file_rename)
            shutil.move(DOWNLOADS+file_rename, file_path+file_rename)
       

class EventHandler(LoggingEventHandler):
    def on_modified(self, event):
        cleanup(IMAGES, image_extensions)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    #logging.info(f'start watching directory {path!r}')
    event_handler = EventHandler()
    path = DOWNLOADS

    #instantiating observer class - watches for any file system changes and then send event to event handler
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        #running indefintely until stopped at terminal
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()



d




#cleanup(IMAGES, image_extensions)
#cleanup(DOCUMENTS, document_extensions)


#Done- creating methods so you can call one method pass in the type of extension and that will execute
#Done- currently i assume if files were named with the extension and the extensions were different - it move wrong files - test this - use lower.endswith('.txt')
#Done- if two files were named the same then it will simply replace - this needs fixing - not actually fixed, temp solution to not copy
#Done- rename file and append random number generator - now completed used seeded random gen to append to file then move to keep both files
# not best solution ideally i will want to check to see if a copy exists in the directory then increment by 1 for every new copy added
# add handler to automatically add to directory when anything new is added