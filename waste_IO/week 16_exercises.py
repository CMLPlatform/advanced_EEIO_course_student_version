"""

EIOA course

Week 16 Exercises - WIOTs 


This module provides a code example to address Part B of week 11 exercises
(i,e., WIOTs).

The module includes:
    A) Import data
    B) Build the WIO model
    C) Calculate the impact of different components of final demand on landfill area

Software version: Phyton 3.8.


Created on Jan 18 10:40:00 2022
Based on 'Lecture 6' from Joao F. D. Rodrigues 
@author: aguilarga 

"""

# Import packages

import pandas as pd
import numpy as np

# A) Import data
data = 'week_16_data.xlsx'
ZYeconomy = pd.read_excel(data, sheet_name = 'ZYeconomy', index_col = 0) # Input-output table, including intermediate and final demand matrix
ZYwaste = pd.read_excel(data, sheet_name = 'ZYwaste', index_col = 0) # Waste account, including intermediate and final demand matrix
F = pd.read_excel(data, sheet_name = 'F', index_col = 0) # VA and satellite account
Q = pd.read_excel(data, sheet_name = 'Allocation', index_col = 0) # Waste allocation matrix
unit = pd.read_excel(data, sheet_name = 'Units', index_col = False) # units

# B) Build WIOT

# First, identify the number of sectors and sector headers
n_e = 103 # number of economic sectors
n_wt = 13 # number of waste treatment sectors
n_y = 11 # number of final demand categories
n_w = 79 # number of waste flows



# Separate Z_e_e, Z_e_wt, Y, Z_wo_e, Z_wi_e, Z_wi_wt, Z_wi_wt, Y_wi, Y_wo

Z_e_e = ZYeconomy.iloc[:, 0:n_e] # IO economy with the 103 economic sectors
Z_e_wt = ZYeconomy.iloc[:, n_e:n_e + n_wt] # IO waste treatment with the 13 waste treatment categories
Y_e = ZYeconomy.iloc[:, n_e+n_wt:n_e+n_wt+n_y] # Final demand matrix
Z_wo_e = ZYwaste.iloc[0:n_w, 0:n_e] # Waste outflow of 103 economic sectors
Z_wi_e = ZYwaste.iloc[n_w:n_w+n_w, 0:n_e] # Waste inflow of 103 economic sectors
Z_wo_wt = ZYwaste.iloc[0:n_w, n_e:n_e+n_wt] # Waste outflow of 13 waste treatments
Z_wi_wt = ZYwaste.iloc[n_w:n_w+n_w, n_e:n_e+n_wt] # Waste inflow of 13 wasre treatments
Y_wo = ZYwaste.iloc[0:n_w, n_e+n_wt:n_e+n_wt+n_y] # Waste outflow of 11 final demand categories
Y_wi = ZYwaste.iloc[n_w:n_w+n_w, n_e+n_wt:n_e+n_wt+n_y] # Waste inflow of 11 final demand categories

# Calculate net waste flows Z_w_e, Z_w_wt, and Y_w

Z_w_e = Z_wo_e.values - Z_wi_e.values # Net waste flow of 103 economic sectors. Note: Here pd.dataframe is coverted first into np.array
Z_w_wt = Z_wo_wt.values - Z_wi_wt.values # Net waste flow of 13 waste treatmets
Y_w = Y_wo.values - Y_wi.values # Net waste flow of 11 final demand categories

# Covert waste flows into waste treatments Z_wt_e, Z_wt_wt, Y_wt
Z_wt_e = Q.values @ Z_w_e  # Matrix of waste flows generated and/or absorbed by 103 economic sector
Z_wt_wt = Q.values @ Z_w_wt  # Matrix of waste flows generated and/or absorbed by 13 waste treatment sectors sector
Y_wt = Q.values @ Y_w  # Matrix of waste flows generated and/or absorbed by 11 final demand categories

# Group matrices in a WIOT arrange

## First, let's create pd.dataframes
Z_wt_e = pd.DataFrame(Z_wt_e, index=Q.index, columns=Z_e_e.columns) 
Z_wt_wt = pd.DataFrame(Z_wt_wt, index=Q.index, columns=Z_e_wt.columns) 
Y_wt = pd.DataFrame(Y_wt, index=Q.index, columns=Y_e.columns) 

wiot_e = pd.concat([Z_e_e, Z_e_wt], axis=1)  # Concat Z_e_e and Z_e_wt block
wiot_wt = pd.concat([Z_wt_e, Z_wt_wt], axis=1) # Concat Z_wt_e and Z_wt_wt block
Z_wiot = pd.concat([wiot_e, wiot_wt], axis=0) # Integrate WIOT
Y_wiot = pd.concat([Y_e, Y_wt], axis=0) # Concat Y_e and Y_wt

# C) Calculate the impact of different components of final demand on landfill area


## Calculate Leontief inverse

x = Z_wiot.sum(axis = 1).values + Y_wiot.sum(axis = 1).values
xinv = np.diag(((x != 0)/(x + (x == 0))).flatten())
A = Z_wiot @ xinv
I = np.identity(len(A))           # An identy matrix of the size as A-matrix
L = np.linalg.inv(I - A)

## Landfill intensity
F = F.iloc[8,: n_e+n_wt] #Landfill area in square meter is in position 8
f = F @ xinv

## Calculate land footprint  per economic sector(LF)

y_sum = Y_wiot.sum(1).values  # Final demand vector
LF = f @ L @ np.diag(y_sum.flatten()) # Landfill footprint calculation
LF = pd.DataFrame(LF, index=Y_wiot.index, columns=['Landfill footprint'])  # Create new dataframe with LF
LF_sort = LF.sort_values(by='Landfill footprint', ascending=False)  # Sort results
print(LF_sort.head(5)) # Print top-5 contributors
