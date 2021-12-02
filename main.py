"""
Created on Wed Nov 24 10:19:00 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti 
          Vadilonga00 : Francesca Vadilonga
"""
import Utils
import pandas as pd



taxi_cols=['tpep_pickup_datetime', 'PULocationID']
zone_cols=['LocationID', 'Borough']


data = Utils.ReadCSVFile("indata/yellow_tripdata_2021-01.csv", taxi_cols)
data.info()
zone_lookup = Utils.ReadCSVFile("indata/taxi+_zone_lookup.csv", zone_cols)
zone_lookup.info()


data['tpep_pickup_datetime']=pd.to_datetime(data['tpep_pickup_datetime'],format="%Y/%m/%d %H:%M:%S")



numero_corse=data.shape[0]