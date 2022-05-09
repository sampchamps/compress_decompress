import os
import glob
import pathlib
import tarfile
import unittest
 
from compress_decompress import *

class TestScan(unittest.TestCase):
    
    def test_decompress(self):
        cd = CompressDecompress()
        outputfolder = "test_decompress"
        outputfile = "test_compress.tar.gz"
        path_parent_folder="/home/digipro/Documents/Digital-Prophets/work/python_tuts/"
        cd.decompress_files(path_parent_folder,outputfile,outputfolder)
        for path_file in os.listdir(outputfolder):
                count = 0
                if os.path.isfile(os.path.join(outputfolder, path_file)):
                    count += 1
                    return(count)
        self.assertIn(outputfolder,path_parent_folder)
       
if __name__ == "__main__":
        TestScan.main()