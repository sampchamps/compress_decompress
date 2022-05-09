import os
import glob
import pathlib
import tarfile
import unittest
 
from compress_decompress import *


class TestScan(unittest.TestCase):
    def test_compress(self):
        cd=CompressDecompress()
        path_parent_folder = "/home/digipro/Documents/Digital-Prophets/work/python_tuts/"
        tar_file = "test_compress.tar.gz"
        cd.compress_files(path_parent_folder, tar_file)
        if cd.compress_files:
            count = 0
            file_extension = pathlib.Path(tar_file).suffix
            for path_file in os.listdir(path_parent_folder):
                if os.path.isfile(os.path.join(path_parent_folder, path_file)):
                    count += 1
                    return(count, file_extension)
        self.assertIn(tar_file,os.listdir(path_parent_folder))


if __name__ == "__main__":
        TestScan.main()
        


