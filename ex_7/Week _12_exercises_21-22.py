# -*- coding: utf-8 -*-
"""
EIOA course

Week 12 Exercises - PIOTs/HIOTs 

This module provides a code example to create a Sankey diagram for the global input-output material flows


The module includes:
    A) Import data
    B) Settings
    C) Sankey diagram with Floweaver (https://floweaver.readthedocs.io/en/latest/sdd.html)

Notes: 
    
- Make sure to install Floweaver (https://floweaver.readthedocs.io/en/latest/installation.html)
- Run function in Jupyter Notebook for better performance of SankeyWidgeand  visualization

      
Database: modification from EXIOBASE HIOT  


Software version: Phyton 3.8.


Created on Jan 13 12:40:00 2022
Updated on Jan 14 07:50:00 2022

@author: aguilarga 

"""
import pandas as pd
import floweaver as fw
from ipysankeywidget import SankeyWidget

# A) IMPORT DATA
df=pd.read_excel("week_12_data.xlsx", index_col=0, header=0)

# B) Settings
flows = pd.DataFrame([['N', 'I&C', 'all_mat', df.iloc[0,0]],
                      ['I&C', 'E', 'all_mat', df.iloc[1,0]],
                      ['I&C', 'T', 'all_mat', df.iloc[2,0]],
                      ['I&C', 'S', 'all_mat', df.iloc[3,0]],
                      ['S', 'T', 'fossil', df.iloc[4,0]],
                      ['T', 'W', 'all_mat', df.iloc[5,0]],
                      ['T', 'I&C', 'all_mat', df.iloc[6,0]]]) # Dataframe in structure required by Floweaver
flows.columns = ['source', 'target', 'type', 'value']

nodes = {'N': fw.ProcessGroup(['N']),
        'I&C': fw.ProcessGroup(['I&C']),
         'S': fw.ProcessGroup(['S']),
         'T': fw.ProcessGroup(['T']),
         'DPO': fw.ProcessGroup(['E', 'W']),
         'rec': fw.Waypoint(direction='L'), } # Nodes = Group of processes from the underlying dataset
ordering = [[['N'], []],
           [['I&C'], ['rec']],
           [['S'], []],
           [['T'], []],
           [['DPO'], []]] # Ordering = The order of processes in the diagram
bundles = [fw.Bundle('N', 'I&C'),
           fw.Bundle('I&C', 'T'),
           fw.Bundle('I&C', 'S'),
           fw.Bundle('I&C', 'DPO'),
           fw.Bundle('S', 'T'),
           fw.Bundle('T', 'DPO'),
           fw.Bundle('T', 'I&C'), ] # Bundle = a set of flows between two processes

# C) Sankey diagram with Floweaver

sdd = fw.SankeyDefinition(nodes, bundles, ordering)  # Connect all settings
size = dict(width=750, height=300)  # Adjust diagram size
fw.weave(sdd, flows, palette=['blue']).to_widget(**size) # Display Sankey diagram
