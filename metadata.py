import subprocess
import glob
import re


imgpath = 'images'
ISOs = []
fmt = 'ARW'
for image in glob.glob(imgpath+'/*.'+fmt):
    cur_out = subprocess.run(['./dcraw', '-v', '-i', image], capture_output=True)
    cur_iso = re.findall("\nISO speed: \d+", cur_out.stdout.decode('utf-8'))
    ISOs.append(int(cur_iso[0].split(': ')[1]))


def get_iso_list(imgpath, camera):

    iso = []

    if camera == 'sony':
        fmt = 'ARW'
    elif camera == 'nikon':
        fmt = 'NEF'
    else:
        print('use sony or nikon for \'camera\' parameter')


    for image in glob.glob(imgpath + '/*.' + fmt):
        cur_out = subprocess.run(['./dcraw', '-v', '-i', image], shell=False, capture_output=True)
        cur_iso = re.findall("\nISO speed: \d+", cur_out.stdout.decode('utf-8'))
        ISOs.append(int(cur_iso[0].split(': ')[1]))
    return iso




def raw_to_tiff_cfa():
    x = "a"


#def raw_to_tiff_debayered


#def tiff_cfa_register

