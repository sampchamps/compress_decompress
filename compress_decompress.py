import os 
import argparse
import tarfile

class CompressDecompress:
    def compress_files(self,path,outputfile):
        """
        Create a Compress file
        """
        path_parent_folder = os.listdir(path)
        files_compress = tarfile.open(outputfile, "w:gz")
        if path_parent_folder:
            for list_of_files in path_parent_folder:
                files_compress.add(list_of_files)
            print("Files have being Compressed")
        else:
            print("Files have not being Compressed")

    def decompress_files(self,path_to_folder,outputfile,outputfolder):
        """
        Decompress files into folder
        """
        files_decompress =  os.listdir(path_to_folder)
        files_decompress = tarfile.open(outputfile)
        if files_decompress:
            files_decompress.extractall(outputfolder)
            print("Files have being Decompressed")
        else:
            print("Files have not being Decompressed")   

def main():
    """
    Main Function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-co","--compress", help="This compress file inside the Directory",action="store_true")
    parser.add_argument("-de","--decompress", help="This decompress file inside the Directory",action="store_true")
    args = parser.parse_args()

    # Calling the class
    cd = CompressDecompress()

    if args.compress:
        cd.compress_files("<path_to folder>","compress.tar.gz" ) 
    elif args.decompress:
        cd.decompress_files("<path_to folder>","compress.tar.gz","decompress_directory")
    else:
        print("Didn't call the required argument name - '-co', '-de'")

if __name__ == '__main__':
    main()