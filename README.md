# Python: PDF to JPG

Made this script for my work to convert pdf files into jpg files. 



## Installation:

Poppler for Mac OSX

```bash
$ brew install poppler
```



 [pdf2image](https://github.com/Belval/pdf2image) module for python

```bash
$ pip install pdf2image
```



Change these variables for system_name and system_path

```python
system_name = 'zowie'  #Current logged in user
system_path = '/Documents/Werk/Stansen/' #Path file needs to be saved
```



## Usage

```bash
$ python convert_pdf_to_jpg.py << path/filename.pdf >>
```

