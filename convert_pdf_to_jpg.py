"""
Case: Convert PDF to JPG
Author: Zowie van Geest

Installation:
Poppler for Mac OSX
$ brew install poppler

pdf2image module for python
$ pip install pdf2image

Tested version:
Python 2.7.15
"""

import sys
import os
import shutil
from pdf2image import convert_from_path

# System name and path declaration

system_name = 'zowie'
system_path = '/Documents/Werk/Stansen/'


def input_diecut():
    while True:
        user_input = str(input('Welk stansnummer hoort hierbij?\n'))
        try:
            if not user_input:
                raise ValueError
        except ValueError:
            print 'Vul een stansnummer in!'
        else:
            return user_input


def convert_pdf_to_jpg(new_path_pdf, new_path_jpg):
    try:
        convert_pdf = convert_from_path(new_path_pdf, 500)
        for page in convert_pdf:
            page.save(new_path_jpg, 'JPEG')
    except Exception, err:
        return False


def copy_rename_file(file_paths):
    try:
        for p in file_paths:
            new_name = input_diecut()
            os.makedirs(new_name)

            # Logging directory's

            print 'Nieuwe bestandsnaam is: ' + new_name + '.pdf'
            print 'En is te vinden in onderstaande map:'

            # Base path and base name

            base_path = '/Users/' + system_name + system_path \
                + new_name + '/'
            base_path_and_name = base_path + new_name

            # New Path for PDF and JPG

            new_path_pdf = base_path_and_name + '.pdf'
            new_path_jpg = base_path_and_name + '.jpg'

            # Check if path dont exists 

            if not os.path.exists(new_path_pdf):
                print new_path_pdf

                # Copy dragged file and save it as new file

                shutil.copyfile(p, new_path_pdf)
                print 'Stans overgezet!'
                
                # Convert PDF to JPG
                
                convert_pdf = convert_pdf_to_jpg(new_path_pdf, new_path_jpg)
    except Exception, err:
        return False


def main():
    file_paths = sys.argv[1:]
    copy_file = copy_rename_file(file_paths)


if __name__ == '__main__':
    main()
