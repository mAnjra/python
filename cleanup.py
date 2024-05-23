import shutil
import os
import random
import time
import logging

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

'''
Download folder cleaner - dumps files into folders
'''
# defualt start point will be system time if no arg passed
random.seed()

#find directory where cleanup.py exist
dir_pth = os.path.dirname(os.path.realpath(__file__))

DOWNLOADS = dir_pth+'/'
IMAGES = '/Users/azhar/Downloads/images/'
DOCUMENTS = '/Users/azhar/Downloads/documents/'
APPLICATIONS = '/Users/azhar/Downloads/applications/'

image_extensions = {'.jpg','.HEIC','.heic','.png'}
document_extensions = {'.pdf', '.txt'}
disk_image_extensions = {'.dmg'}




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

def run_cleanup():
    cleanup(IMAGES, image_extensions)
    cleanup(DOCUMENTS, document_extensions)
    cleanup(APPLICATIONS, disk_image_extensions)


while True:
    use_handler = input("Activate event handler:(Y/n)")
    if use_handler == "Y":
        break
    elif use_handler == "n":
        run_cleanup()
        break
    else:
        print("Please use either uppercase Y or lowercase n")
    

class EventHandler(LoggingEventHandler):
    def on_modified(self, event):
        run_cleanup() 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    if use_handler == "Y":
        print("Watchdog Activated")
        run_cleanup()
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
    else:
        print("Watchdog not activated")


#Done- creating methods so you can call one method pass in the type of extension and that will execute
#Done- currently i assume if files were named with the extension and the extensions were different - it move wrong files - test this - use lower.endswith('.txt')
#Done- if two files were named the same then it will simply replace - this needs fixing - not actually fixed, temp solution to not copy
#Done- rename file and append random number generator - now completed used seeded random gen to append to file then move to keep both files
# not best solution ideally i will want to check to see if a copy exists in the directory then increment by 1 for every new copy added
#Done- add handler to automatically add to directory when anything new is added
#Done- Adding an option to activate watchdog or just cleanup and leave
# when watchdog not activated count how many files were moved and print alongside current message to give an idea