from PIL import Image

import os



L = os.listdir('/home/bryan/Downloads/fish_datas/NA_Fish_Dataset/')

os.makedirs('/home/bryan/Downloads/fish_datas/NA_Fish_Dataset/new_data')

for i in L:
    l = os.listdir('/home/bryan/Downloads/fish_datas/NA_Fish_Dataset/%s' %i)
    os.makedirs('/home/bryan/Downloads/fish_datas/NA_Fish_Dataset/new_data/%s' % i, exist_ok=False)

    for x in l:
        img = Image.open('/home/bryan/Downloads/fish_datas/NA_Fish_Dataset/%s/%s' % (i, x))
        img_resize = img.resize((256, 256))

        img_resize.save('/home/bryan/Downloads/fish_datas/NA_Fish_Dataset/new_data/%s/%s' %(i,x))
