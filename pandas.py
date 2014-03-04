# конспект видео с ВесМакинзи http://www.youtube.com/watch?v=w26x-z-BdWQ

# Series
import pandas as pd

labels = [2009, 2010, 2011, 2012]
s = pd.Series(random.randn(4), index = labels)
2011 in s # True

print s.index # yeilds index object
mydict = s.to_dict() 
s.to_csv()

# labeled series from dict!
minis = Series(mydict, index = [2010,2012, 2014])
# if not in dict will be NaN (a float)
pd.isnull(minis) # shows True/False for NaN value
minis[pd.isnull(minis)] #only elements that are NaN
minis[pd.notnull(minis)] # minis.dropna() does the same
s * 2 # numpy-like applies to each element
minis.head() # lists first few elements 


# DateFrame: 2Dcollection of Series
# pass dict with elements as lists of same size
df = pd.DateFrame({'a':np.random.randn(6), 
    'b': ['foo','bar']*3, 'c':np.random.randn(6)})
df['b'] # series for 'b' column
# adding new column by treating like dict
df['d'] = range(6) # added new column
df[5:6] df.xs(5) # get 5th row

df.ix[0] # first raw
df.ix[2,'b'] #specifc element
df.get_value(2,'b') #also ok, quicker
df.ix[2:4,['b','c']]  
df.ix[df['c']>0, ['b','c']]

# time series indexes
df=DateFrame(.., index=DateRange('1/1/2000', periods=6))
# column labels
df=DateFrame(.., columns=['a','b'])

# read DateFrme from csv
close_px=pd.read_csv('file.csv',index_col=0,parse_dates=True)
# idex_col for column taken as index

s1 + s2 # sum of series gives proper merged union of the dates
# Nan for ones without matching dates
s1.add(s2,fill_value=0)

df.apply(np.mean) # applies function to each column
df[['AAPL','IBM']].plot()












