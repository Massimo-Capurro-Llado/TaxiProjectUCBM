# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:43:31 2021

@author: carpy
"""
import Utils
import glob
import pandas as pd
def read_multiple_file(parser):#da risolvere problema mese,borough
    filenames = glob.glob(parser.path + "/*.csv")
    taxi_cols=['tpep_pickup_datetime','PULocationID']
    dfs = []
    for i in parser.month:
        dfs.append(Utils.ReadCSVFile(filenames[int(i)], taxi_cols))
    
    # Concatenate all data into one DataFrame
    big_frame = pd.concat(dfs, ignore_index=True)
    return big_frame