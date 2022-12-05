# -*- coding: utf-8 -*-
"""
EIOA course

Week 19 Exercises - Modelling circular economy

Goal 1: Create a function to model circular economy interventions using Pandas

This module includes:
    
    A) Import data
    B) Footprint function
    C) Function final demand changes
    D) Modelling product lifetime extension
@author: aguilarga


"""

#Import packages
import pandas as pd
import numpy as np

# A) Import data
A = pd.read_excel('week_19_data.xlsx', sheet_name = 'A', index_col = 0) # Loading A matrix
Y = pd.read_excel('week_19_data.xlsx', sheet_name = 'Y', index_col = 0) # Loading Y matrix
f = pd.read_excel('week_19_data.xlsx', sheet_name = 'f', index_col = 0) # Loading f matrix
F_hh = pd.read_excel('week_19_data.xlsx', sheet_name = 'F_hh', index_col = 0) # Loading F_HH matrix

# B) Footprint function

def footprint(impact):
    #Load the data files
    A = pd.read_excel('week_19_data.xlsx', sheet_name = 'A', index_col = 0)
    Y = pd.read_excel('week_19_data.xlsx', sheet_name = 'Y', index_col = 0)
    f = pd.read_excel('week_19_data.xlsx', sheet_name = 'f', index_col = 0)
    F_hh = pd.read_excel('week_19_data.xlsx', sheet_name = 'F_hh', index_col = 0)
    # Calculating total impact
    ID = np.identity(A.shape[1])  # Identity matrix
    L = np.linalg.inv(ID-A)  # L matrix
    L = pd.DataFrame(L, index=A.index, columns=A.columns) # Making L-matrix a pd.DataFrame to use '.dot' in the matrix multplication below
    r_ = f.dot(L).dot(Y) # fLy calculation for all environmental indicators
    r = r_.loc[impact, :].sum() + F_hh.loc[impact, :].sum() # Footprint calculation for the specific impact category 
    return r.round(1) # result rounded to one decimal

fp_co2 = footprint('CO2') # example of using footprint function for CO2 impacts
fp_ene = footprint('Energy') # example of using footprint function for Energy impacts

# C) Changes in final demand function

def footprint_alt(ori, k, sub, alpha, impact):
    #Load the data files
    A = pd.read_excel('week_19_data.xlsx', sheet_name = 'A', index_col = 0)
    Y = pd.read_excel('week_19_data.xlsx', sheet_name = 'Y', index_col = 0)
    f = pd.read_excel('week_19_data.xlsx', sheet_name = 'f', index_col = 0)
    F_hh = pd.read_excel('week_19_data.xlsx', sheet_name = 'F_hh', index_col = 0)
    #Modelling substitution in final demand
    Y_new = Y.copy(deep=True) # copy of Y vector
    Y_new.loc[ori, :] = Y_new.loc[ori, :].sum()*(1 - k) # Selecting original sector and applying change coefficient 
    Y_new.loc[sub, :] = (Y_new.loc[sub, :].sum() + 
                        (Y.loc[ori, :].sum() - Y_new.loc[ori, :].sum())*alpha) # Selecting substition sector and applying substitution weighting factor
    #Calculating total impact
    ID = np.identity(A.shape[1])  # Identity matrix
    L = np.linalg.inv(ID-A)  # L matrix
    L = pd.DataFrame(L, index=A.index, columns=A.columns) # Making L-matrix a pd.DataFrame to use '.dot' in the matrix multplication below
    r_ = f.dot(L).dot(Y_new) # fLy calculation with changes in final demand
    r = r_.loc[impact, :].sum() + F_hh.loc[impact, :].sum() # Footprint calculation with changes in final demand
    return r.round(1) # result rounded to one decimal

# D)Modelling product lifetime extension
    
ori = 'Passenger motor cars' # origal sector label
sub = 'Repair of motor vehicles and machine' # substition sector
k = 0.80 # change coeffient
alpha = 0.4 # substitution weighting factor

fp = footprint('CO2') # original CO2 footprint
fp_alt = footprint_alt(ori, k, sub, alpha, 'CO2') # alternative CO2 footprint
change = (fp_alt - fp) # Footprint change
change_per = change/fp*100 # Footprint change in percentage
