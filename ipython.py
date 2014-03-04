ipython notebook
# Tab autocomplete is amazing
# exception messages r beautiful
%pylab inline #embed plots into notebook

; to surpress output
_ - last output value
Out[16] labeled output
%quickref #cheatsheet for ipython
%magic #reference for magic commands
%lsmagic
%bash #this cell is bash interpreted!!
%timeit


%reset # flushes everything in memory
%history # all executed commands (like to copypaste to editor)
%history -l 20 -f file.py # last 20 lines to file.py


files = !ls #assign from shell!!
!echo $files #..and back!

import collections
collections.namedtuple?  # docs screen for anything
collections.namedtuple?? # gets to source code 
numpy.*cos*? # all objects containing cos

