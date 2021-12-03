# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:43:31 2021

@author: carpy
"""
import Utils
import pandas as pd

taxi_cols=['tpep_pickup_datetime', 'PULocationID']
zone_cols=['LocationID', 'Borough']


#TODO: Integrate Borough
def statistics(parser):

    result=[]
    for i in parser.month:
        month_data = Utils.readCSVFile(parser.path + f'/yellow_tripdata_{parser.year}-0{i}.csv', taxi_cols)
        month_data['tpep_pickup_datetime']=pd.to_datetime(month_data['tpep_pickup_datetime'],format="%Y/%m/%d %H:%M:%S")
        month_data['month'] = month_data['tpep_pickup_datetime'].dt.month
        month_data['day'] = month_data['tpep_pickup_datetime'].dt.day
        giorni_del_mese = max(month_data['day'])
        result.append(round(month_data.shape[0]/giorni_del_mese))
        period = result.index(max(result))+1
        
        
    zone_lookup = Utils.readCSVFile("Specifiche/taxi+_zone_lookup.csv", zone_cols)
    zone_lookup.info()
    
    return result, period

