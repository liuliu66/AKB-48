import os
files = os.listdir('.')
for file in files:
    if file.endswith('.png'):
        box_name_org = file.split('.')[0]
        box_id_org = int(box_name_org.split('box')[1])
        box_id_new = box_id_org + 8
        box_name_new = 'box' + str(box_id_new)
        # os.makedirs(box_name_new)
        os.rename(file, os.path.join(box_name_new, box_name_new+'.png'))