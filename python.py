#!/usr/bin/env python
# -*- coding: utf-8 -*-
# or to emphasize its python2
#!/usr/bin/python2



# gives float in seconds
import time; time.time()
del a['b'] # delete key in dict
!head -n 10 file.csv # in ipython run shell commands with !command

# character is the carriage return
'\r' 
# enumerate
for i, x in enumerate(listik):

###############################
# json'чики
import simplejson
a= simplejson.dumps(dictionary)
simplejson.loads(a)

###############################
# command line argument
sys.argv[1]

###############################
# %s for strings, %d for integers, %v for floats, if several tuple
print 'File title: %s and %d ' % (title, digit)

###############################
# clears whitespace
'whoah \n'.rstrip()
unichr(62) == u'>' # int to unicode character
chr(62) == '>' # ..to ansii

###############################
# разделить на лист строчечек
"line1 \n line2 \r \n line3 \n line 4".splitlines()
["Hello","Dima"],join(',') # лист строчек слить в один текст
"Hello Dima".replace("Dima","Dmitry")
a = [4,6,78].copy() # не пойнтер, а прямо весь новый лист

###############################
# docstrings (документация)
def lower_case_really():
    """ Here is the docstring"""

###############################
# import os
os.listdir() # список файлов в директории
os.environ.copy() # список глобальных констант в виде dict
os.getcwd()

###############################
print 22 >> 1 #11, cдвигает регистр двоичного представления

###############################
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)


#Named tuples
from collections import namedtuple
Log = namedtuple("LogEntry", ("level", "message"))


###############################
#Three modules you absolutely need:unittest, mock and coverage. 
#Its amazing how many bugs you can find by going for (near)
# 100% code coverage.

# using zip to invert dict
mi = dict(zip(m.values(), m.keys()))
mi = {v: k for (k, v) in m.iteritems()}

# flatten a list
a = [[1, 2], [3, 4], [5, 6]]
>>> b = [x for l in a for x in l]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]

