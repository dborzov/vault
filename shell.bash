#!/bin/bash
#----------------------------------------------
## Detect file encoding
file -I word_corpus.txt
# word_corpus.txt: text/plain; charset=us-ascii
#----------------------------------------------
## Make executable
chmod 755 myscript.sh 
#----------------------------------------------
