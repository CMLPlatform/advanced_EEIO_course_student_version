"""
EIOA course

Week 10 Exercises - EXIOBASE introduction 

This module provides a code example to address Part B of week 7 exercises
(i,e., EXIOBASE introduction).


The module includes:
    A) Import data
    B) Select specific countries with Pandas
    C) Selecte specific commodities with Pandas
    D) Calculate Leontief inverse 
    E) Calculate total output vector

Database:   https://www.exiobase.eu/index.php


Software version: Phyton 3.8.


Created on Jan 06 08:57:00 2022
@author: aguilarga 

"""
# IMPORT PACKAGES

import pandas as pd           # shortening "pandas" to "pd" to make code easier to read
import numpy as np            # shortening "numpy" to "np" to make code easier to read


## VERY IMPORTANT: save and unzip the data files to the current working directory; you can set the current
## working directory at the top right of the screen in Spyder

# Briefly, first read (tab delimited) data as DataFrame, which is a data strcuture in the Pandas library, 
# and then convert the DataFrame to numpy array. To learn more about DataFrame and read_csv check here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html.  

# A) Import data

path = 'IOT_2011_pxp'    # add name of folder where data is stored                                
A = pd.read_csv(path + '/A.txt', sep='\t',
                index_col=[0, 1], header=[0, 1])  # Z matrix
Y = pd.read_csv(path + '/Y.txt', sep='\t',
                index_col=[0, 1], header=[0, 1])  # y matrix
F = pd.read_csv(path + '/satellite/F.txt', sep='\t',
                index_col=[0], header=[0, 1])  # satellite matrix
F_hh = pd.read_csv(path + '/satellite/F_hh.txt', sep='\t',
                index_col=[0], header=[0, 1])  # satellite for FD matrix

# B) Select specific countries with Pandas

country = 'NL'           #country variable
y_c = Y.loc[:, country]  # All final demand categories for a specifc cuntry
y_c_total = y_c.sum(1)   # Sum of final demand per commodity

# C) Selecte specific commodities with Pandas

product = 'Office machinery and computers (30)'  # Commodity variable. This is taken from EXIOBASE labels
y_c_p = y_c_total.loc[:, product]   # Total final demand of specific commodity per country/region


# D) Calculate Leontief inverse

I = np.identity(len(A))           # An identy matrix of the size as A-matrix
L = np.linalg.inv(I - A)

# E) Calculate total output vector (X)

y_total = Y.sum(1)      # Sum of all final demand categories
x = L @ y_total         # Total outputs
df_x = pd.DataFrame(x)  # Total outputs as dataframe
df_x.index = Y.index    # Adding labels to rows



