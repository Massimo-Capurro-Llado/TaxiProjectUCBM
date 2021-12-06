# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:43:31 2021

@author: carpy
"""
import Utils
import pandas as pd
import matplotlib.pyplot as plt

taxi_cols=['tpep_pickup_datetime', 'PULocationID']
zone_cols=['LocationID', 'Borough']


#TODO: Integrate Borough
def statistics_per_month(parser):
# =============================================================================
#     zone_lookup = Utils.readCSVFile(parser.zone, zone_cols)
#     correct_borough = zone_lookup['Borough'].isin(parser.borough)
#     id_list = zone_lookup[correct_borough]['LocationID'].tolist()
#     print(id_list)
# =============================================================================
    #result=[]
    #for i in parser.month:
        
    month_data = Utils.readCSVFile(parser.path + f'/yellow_tripdata_{parser.year}-0{6}.csv', taxi_cols)
    month_data['tpep_pickup_datetime']=pd.to_datetime(month_data['tpep_pickup_datetime'],format="%Y/%m/%d %H:%M:%S")
    giorni_del_mese =max(month_data['tpep_pickup_datetime'].dt.day)
    #giorni_del_mese = max(month_data['day'])
        
            # calculate the trips per day of the i-th month
            #result.append(round(month_data.shape[0]/giorni_del_mese))
            #period = result.index(max(result))+1
        
            # calculate the trips of the borough of the i-th month
# =============================================================================
#             trips_per_borough=month_data.iloc[:,[1]].value_counts().to_dict()
#             borough=borough.append(trips_per_borough,ignore_index=True)
# =============================================================================
            # TODO: chamge name of the columns before transoping   (from 0 to 1 )
            #  TODO: fix formatting of the results index
# =============================================================================
#             result_borough=borough.transpose()
# =============================================================================
    return month_data, giorni_del_mese #period , #result_borough

def stats_per_borough(parser,month_data,giorni_del_mese):
    zone_lookup = Utils.readCSVFile(parser.zone, zone_cols)
    borough_data  = pd.merge(month_data, zone_lookup, left_on='PULocationID',right_on='LocationID')
    borough_data = borough_data.drop(['PULocationID','LocationID'],axis=1)
    mean_trip_per_borough = {}
    for i in parser.borough:
        mean_trip_per_borough[i] = round(borough_data[borough_data['Borough']==i].shape[0]/giorni_del_mese)
    return mean_trip_per_borough, borough_data

def grafica_mese(mean_trip_per_borough):
    a = plt.bar(mean_trip_per_borough.keys(), mean_trip_per_borough.values(), color='g')
    return a