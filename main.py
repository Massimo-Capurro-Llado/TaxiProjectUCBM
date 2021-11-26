"""
Created on Wed Nov 24 10:19:00 2021

@author: massi
"""
import Utils
import pandas as pd

data = Utils.ReadCSVFile("indata/yellow_tripdata_2021-03.csv")
print(data.head(), '\n\n')
data.info()
zone_lookup = Utils.ReadCSVFile("indata/taxi+_zone_lookup.csv")
zone_lookup.index_col="LocationID"
print(zone_lookup.head())
