"""
EIOA course

Week 11 Exercises - MRIO seminal works

This module provides a code example to address Part B of week 5 exercises
(i,e., MRIO seminal).


The module includes:
    A) Import data
    B) Calculate Leontief inverse and environmental intesity matrix
    C) Final demand contribution to environmental footprint

Database:   


Software version: Phyton 3.8.


Created on Dec 14 12:40:00 2021
Updated on Feb 10 21:00:00 2022
Based on 'Week 4 exercises' from Wang 
@author: aguilarga 

"""
# IMPORT PACKAGES

import pandas as pd 
import numpy as np



## VERY IMPORTANT: save and unzip the data files to the current working directory; you can set the current
## working directory at the top right of the screen in Spyder

# Briefly, first read (tab delimited) data as DataFrame, which is a data strcuture in the Pandas library, 
# and then convert the DataFrame to numpy array. To learn more about DataFrame and read_csv check here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html.  

# A) IMPORT DATA

path = 'IOT_2011_pxp'    # add name of folder where data is stored                                
A = pd.read_csv(path + '/A.txt', sep='\t',
                index_col=[0, 1], header=[0, 1])  # Z matrix
Y = pd.read_csv(path + '/Y.txt', sep='\t',
                index_col=[0, 1], header=[0, 1])  # y matrix
F = pd.read_csv(path + '/satellite/F.txt', sep='\t',
                index_col=[0], header=[0, 1])  # satellite matrix
F_hh = pd.read_csv(path + '/satellite/F_hh.txt', sep='\t',
                index_col=[0], header=[0, 1])  # satellite for FD matrix

# B) CALCULATE LEONTIEF INVERSE AND ENVIRONMENTAL INTENSITY MATRIX

## Leontief inverse matrix
I = np.identity(len(A))           # An identy matrix of the size as A-matrix
L = np.linalg.inv(I - A)

# Calculate total output vector (x)

y_total = Y.sum(1)      # Sum of all final demand categories
x = L @ y_total         # Total outputs


## Environmental intensities

co2_lab = 'CO2 - combustion - air'
F_co2 = F.loc[co2_lab, :]  # select CO2 vector
f_co2 = F_co2/x.transpose() # co2 intensity vector
f_co2 = f_co2.replace([np.inf, -np.inf], np.nan).replace(np.nan, 0)  # replacing inf, -inf, and nan with zeros

# C) FINAL DEMAND CONTRIBUTE TO CO2 FOOTPRINT

## Calculation y_hh, y_gov, and y_cap
hh_lab = 'Final consumption expenditure by households' 
gov_lab = 'Final consumption expenditure by government'	
cap_lab = 'Gross fixed capital formation'

y_hh = Y.xs(hh_lab, axis=1, level=1, drop_level=False)  # selecting hh columns for all countries/regions
y_hh = y_hh.sum(1)  # global final expenditure by household 

y_gov = Y.xs(gov_lab, axis=1, level=1, drop_level=False)  # selecting gov columns for all countries/regions
y_gov = y_gov.sum(1)  # global final expenditure by household 

y_cap = Y.xs(cap_lab, axis=1, level=1, drop_level=False)  # selecting cap columns for all countries/regions
y_cap = y_cap.sum(1)  # global capital formation 


## Calculation CO2 footprint per final demand category per product

co2_hh = f_co2 @ L @ np.diag(y_hh) # CO2 footprint by household expenditures
co2_gov = f_co2 @ L @ np.diag(y_gov) # CO2 footprint by goverment expenditures 
co2_cap = f_co2 @ L @ np.diag(y_cap) # CO2 footprint by capital formation 

## Reshape vectors

co2_hh = np.array(co2_hh).reshape(49,200) # reshape to 49 countries/regions and 200 products
co2_hh_sum = np.sum(co2_hh, axis=0) # sum per product category

co2_gov = np.array(co2_gov).reshape(49,200) # reshape to 49 countries/regions and 200 products
co2_gov_sum = np.sum(co2_gov, axis=0) # sum per product category

co2_cap = np.array(co2_cap).reshape(49,200) # reshape to 49 countries/regions and 200 products
co2_cap_sum = np.sum(co2_cap, axis=0) # sum per product category


## Build new pandas dataframe

df = pd.DataFrame([co2_hh_sum, co2_gov_sum, co2_cap_sum])

### Index product categories

ext_ind = list(range(0,41)) # extraction categories (including agriculture, and mining)
man_ind = list(range(41,149)) # manufacturing (including food, clothing, other products)
con_ind = list(range(149,151)) # construction categories
ser_ind = list(range(151,200))  # services categories

## Sum per product group

ext = df.iloc[:, ext_ind].sum(1)
man = df.iloc[:, man_ind].sum(1)
con = df.iloc[:, con_ind].sum(1)
ser = df.iloc[:, ser_ind].sum(1)

## Re-group dataframe and add labels

df_new = pd.concat([ext, man, con, ser], axis=1)
df_new.index = ['Households', 'Goverment', 'Investment']
df_new.columns = ['Agriculture and Mining', 'Manufacturing', 'Construction', 'Services']


## Create a vertical bar chart
ef_name = 'CO2 footprint (tonnes)'
fig = df_new.plot.barh(stacked=True)
fig.set_xlabel("CO2 footprint (kg)")
fig.set_ylabel(ef_name)
fig.set_title(ef_name + " per final demand category")
fig.legend(loc='center left', bbox_to_anchor=(1, 0.5))
