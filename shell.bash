#!/bin/bash
#----------------------------------------------

## Detect file encoding
file -I word_corpus.txt
# word_corpus.txt: text/plain; charset=us-ascii

## Make executable
chmod 755 myscript.sh 
#----------------------------------------------


# plots tree directory structure
tree -a

# lookup who occupies the port
lsof -i :5002

# kill process by PID
kill -9 PID


# if I want to combine stderr and stdout into the stdout stream
# for further manipulation, I can append the following on the end of my command: 2>&1
python 2>&1

find . -name '*.pyc' -delete # delete with subfolders

# list enviroment variables
env
EDITOR=subl -w # editor for git stuff


hostname # see hostname

pip install -r requirements.txt # reqierements

python -v #versioning

date #timestamp

python -m SimpleHTTPServer
(cd public && python -m SimpleHTTPServer)