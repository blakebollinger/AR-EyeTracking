import numpy as np
import cv2 as cv
from file_methods import load_pldata_file

pupilData = load_pldata_file('./', 'gaze')

f = open('decoded_gaze_data.txt', 'w+')

for datum in pupilData.data:
    for attr in datum.items():
        if(attr[0] != 'base_data'):
            f.write(str(attr) + '\n')

    f.write("\n'base_data':\n")

    for attr in datum['base_data'][0].items():
        f.write(str(attr) + '\n')
    
    f.write('\n-----------------------------------------\n')