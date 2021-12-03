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
    zone_lookup = Utils.readCSVFile(parser.zone, zone_cols)
    correct_borough = zone_lookup['Borough'].isin(parser.borough)
    id_list = zone_lookup[correct_borough]['LocationID'].tolist()
    print(id_list)
    result=[]
    for i in parser.month:
        month_data = Utils.readCSVFile(parser.path + f'/yellow_tripdata_{parser.year}-0{i}.csv', taxi_cols)
        month_data['tpep_pickup_datetime']=pd.to_datetime(month_data['tpep_pickup_datetime'],format="%Y/%m/%d %H:%M:%S")
        month_data['month'] = month_data['tpep_pickup_datetime'].dt.month
        month_data['day'] = month_data['tpep_pickup_datetime'].dt.day
        giorni_del_mese = max(month_data['day'])
        result.append(round(month_data.shape[0]/giorni_del_mese))
        period = result.index(max(result))+1
        
        
   
    
    return result, period

