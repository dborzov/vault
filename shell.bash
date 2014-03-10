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