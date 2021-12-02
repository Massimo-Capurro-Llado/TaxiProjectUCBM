"""
Created on Wed Nov 24 10:19:00 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti 
          Vadilonga00 : Francesca Vadilonga
"""
import Utils
import pandas as pd


#Constanti
taxi_cols=['tpep_pickup_datetime', 'PULocationID']
zone_cols=['LocationID', 'Borough']
parser= Utils.initializeParser()


#Funzione che si occupa della lettura di piu file e dell'esecuzione del programma
def ReadMultipleFiles(parser):
    
    for i in parser.month:
        month_data = Utils.ReadCSVFile(parser.path + f'/yellow_tripdata_{parser.year}-0{i}.csv', taxi_cols)
        month_data['tpep_pickup_datetime']=pd.to_datetime(month_data['tpep_pickup_datetime'],format="%Y/%m/%d %H:%M:%S")
        numero_corse=month_data.shape[0]
        print(numero_corse)
        
    zone_lookup = Utils.ReadCSVFile("indata/taxi+_zone_lookup.csv", zone_cols)
    zone_lookup.info()


ReadMultipleFiles(parser)

