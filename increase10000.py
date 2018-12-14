import os
from astropy.io import fits


script_dir = os.path.dirname(__file__)
correction_folder = os.path.join(script_dir, 'corrected_FITS/')
if not os.path.isdir(correction_folder):
    os.makedirs(correction_folder)

data_path = script_dir + '/Data_low_value/'
filenames = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]

for index in range(len(filenames)):
    if index % 2 == 0:
        hG = fits.getheader(data_path + filenames[index])
        hR = fits.getheader(data_path + filenames[index + 1])
        imG = fits.getdata(data_path + filenames[index])
        imR = fits.getdata(data_path + filenames[index + 1])
        
        imR *= 10000
        imG *= 10000
        
        hduG, hduR = fits.PrimaryHDU(imG, header=hG), fits.PrimaryHDU(imR, header=hR)
        hduG = fits.HDUList([hduG])
        hduG.writeto(correction_folder + str(filenames[index])) 
        hduR = fits.HDUList([hduR])
        hduR.writeto(correction_folder + str(filenames[index + 1]))
