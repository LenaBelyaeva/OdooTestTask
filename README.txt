Python version: 3.6


-----how to work with task6.py-----

1. run task6.py from a directory you want to work with. The script operates with the files in your current directory.
2. There should be a config file "config.par" in the directory, which is used to decide what to do with the files

config.par format:

<extension_1> <COMMAND> <path>
...
<extension_N> <COMMAND> <path>


availible commands: MOVE, COPY, REMOVE
<path> should already exist

for example:

png MOVE C:\OdooTestTask\img
jpg REMOVE
py COPY C:\OdooTestTask\py

3.Input the filenames to work with separated by spaces (type *.* for all files in the folder)
possible formats: *.<file_ext>, <filename>.*,  <filename>.<file_ext>
for example: 
1.png 2.jpg *.doc 3.*