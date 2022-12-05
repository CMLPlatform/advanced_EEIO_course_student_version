import pandas as pd           # shortening "pandas" to "pd" to make code easier to read
import numpy as np            # shortening "numpy" to "np" to make code easier to read

## VERY IMPORTANT: save and unzip the data files to the current working directory; you can set the current
## working directory at the top right of the screen in Spyder

#%%

# Option1：using the '/s+' delimiter means any space is seen as a delimiter, using this
# will not result in a column of NaN values.
df = pd.read_csv('Z.txt', delimiter='\s+', header = None) 
Z = df.to_numpy()

# Option 2: using the '/t' delimiter means any tabs are seen as delimiters, using this
# will result in a column of NaN values (because there are tabs at the end
# of each row.)
df = pd.read_csv('Z.txt', delimiter='\t', header = None)
Z = df.to_numpy()
# np.delete will remove a row or column at the given index (in this case, -1 
# means we are targetting the last item of a list.)
Z = np.delete(Z, obj=-1, axis=1)

#Option 3:
df = pd.read_csv('Z.txt', delimiter='\t', header = None)
# dropna() will drop/remove a column or row depending on the options set
# 'how=all' means the column is only dropped if all the values in it are NaN.
df = df.dropna(axis=1, how="all")
Z = df.to_numpy()

#%%

df = pd.read_csv('x.txt', delimiter='\t', header = None)
x = df.to_numpy()
x = np.delete(x, obj=-1, axis=1)

df = pd.read_csv('Y.txt', delimiter='\t', header = None)
Y = df.to_numpy()
Y = np.delete(Y, obj=-1, axis=1)

df = pd.read_csv('Yt.txt', delimiter='\t', header = None)
Yt = df.to_numpy()
Yt = np.delete(Yt, obj=-1, axis=1)

df = pd.read_csv('F.txt', delimiter='\t', header = None)
F = df.to_numpy()
F = np.delete(F, obj=-1, axis=1)

df = pd.read_csv('Fhh.txt', delimiter='\t', header = None)
Fhh = df.to_numpy()
Fhh = np.delete(Fhh, obj=-1, axis=1)

df = pd.read_csv('pop.txt', delimiter='\t', header = None)
pop = df.to_numpy()
pop = np.delete(pop, obj=-1, axis=1)

# you can quickly check the data type, shape (size), and values of the variables in 'variable explorer'


