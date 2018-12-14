import os
from astropy.io import fits
from astropy.visualization import *
import matplotlib.pyplot as plt
plt.ion()

script_dir = os.path.dirname(__file__)
image_folder = os.path.join(script_dir, 'HiPS/')
if not os.path.isdir(image_folder):
    os.makedirs(image_folder)

data_path = script_dir + '/Data/'
filenames = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]

for index in range(len(filenames)):
    if index % 2 == 0:
        hG = fits.getheader(data_path + filenames[index])
        hR = fits.getheader(data_path + filenames[index + 1])
        imG = fits.getdata(data_path + filenames[index])
        imR = fits.getdata(data_path + filenames[index + 1])
        
        if 'BACKVAL' not in hR:
            imR *= 10000
            imG *= 10000
        else:        
            imR -= float(hR['BACKVAL'])
            imG -= float(hG['BACKVAL'])
        
        try:        
            r = imR.copy()
            b = imG.copy()
            b *= 1.2
            g = (r+b)*0.5
             
        
            q = 12
            s = 170
            m = 15
            
            rgb = make_lupton_rgb(r,g,b,Q=q,stretch=s,minimum=m, 
                                  filename = image_folder + str(filenames[index])[:-6] + ".png") #[:-6] to get rid of file extension
            
            print("Image made")
            
        except:
            print("Image data for r and b are different shapes. Skipping image and moving on...");
