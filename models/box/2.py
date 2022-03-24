import os
import shutil

start_id = 9
folders = os.listdir('.')
for folder in folders:
    if 'box' in folder:
        box_id = int(folder.split('box')[1])
        if box_id >= start_id:
            src = 'box5/index.html'
            dct = '{}/index.html'.format(folder)
            print(src, dct)
            shutil.copy(src, dct)