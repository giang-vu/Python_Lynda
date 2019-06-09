#
# Example file for working with filesystem shell methods
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # Make a duplicate of an existing file
    if path.exists("file1.txt"):
        # Get the path to the file in the current directory
        src = path.realpath("file1.txt")
        
        # Let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"
                
        # Copy over the permissions, modification times, and other info
        shutil.copy(src, dst)
        shutil.copystat(src, dst)
    
        # Rename the original file
        os.rename("file1.txt.bak", "newfile1.txt.bak")
        
        # Now put things into a ZIP archive
        directory, filename = path.split(src)
        make_archive("archive", "zip", directory)

        # more fine-grained control over ZIP file
        with ZipFile("zipfile.zip", "w") as newzip:
            newzip.write("file1.txt")
            newzip.write("newfile1.txt.bak")

if __name__ == "__main__":
    main()
