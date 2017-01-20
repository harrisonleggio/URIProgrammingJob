import os
import shutil
import subprocess
import zipfile
import glob


def main():
    directory = "/shareddata/SRTMv4.1/6_5x5_TIFs"
    #directory = "/Users/student/Desktop/test"
    os.chdir(directory)
    tif_to_grd(directory)




def tif_to_grd(directory):
    for filename in os.listdir(directory):
        #if filename.endswith('.zip'):
        zip_path = os.path.abspath(filename)
        zip_ref = zipfile.ZipFile(zip_path, 'r')
        zip_ref.extractall('/Users/student/Desktop/unzipped_files')
        zip_ref.close()
        for filename in os.listdir('/Users/student/Desktop/unzipped_files'):
            if 'tif' not in filename:
                os.remove('/Users/student/Desktop/unzipped_files/' + str(filename))




if __name__ == '__main__':
    main()