"""
Created on Wed Nov 24 11:06:08 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti 
          Vadilonga00 : Francesca Vadilonga
"""

import pandas as pd
import sys
import argparse


def initializeParser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i1", "--path",
                        help="Path of the directory where the files are",
                        type=str,
                        default='./indata')

    parser.add_argument("-i2", "--month",
                        help="The months to put under analysis",
                        type=list,
                        default='123456')

    parser.add_argument("-i3", "--year",
                        help="The year to put under analysis",
                        type=int,
                        default="2021")

    parser.add_argument("-i4", "--zone",
                        help="The zone_lookup file with information about the Borough",
                        type=str,
                        default='Specifiche/taxi+_zone_lookup.csv')

    parser.add_argument("-i5", "--borough",
                        help="The zone_lookup file with information about the Borough",
                        type=list,
                        default=['Manhattan', 'Queens', 'EWR', 'Bronx', 'Staten Island', 'Brooklyn'])

    parser.add_argument("-e", "--extension",
                        help="Input file extension, including dot (Es -> .csv)",
                        type=str,
                        default='.csv')

    return parser.parse_args()


# This function reads the csv files of taxi trips and Borough and merges teh useful data into a dataframe

def read_csv(file, zone):
    try:
        taxi_data = pd.read_csv(file, usecols=['tpep_pickup_datetime', 'PULocationID'])
        zone_lookup = pd.read_csv(zone, usecols=['LocationID', 'Borough'])
        return pd.merge(taxi_data, zone_lookup, left_on='PULocationID', right_on='LocationID')
    except OSError as e:
        print(e)
        sys.exit()

# This function creates a dictionary of (key:month, value: name of the month related file)

def get_files_list(parser):
    fileList = {}
    for m in parser.month:
        n = str(m).zfill(2)
        fileList[m] = parser.path + f'/yellow_tripdata_{parser.year}-{n}.csv'
    return fileList

def data_cleaner(month_data,parser,month):
    #take the first coloum of month_data dataframe named ['tpep_pickup_datatime']
    month_data.iloc[:,0] = pd.to_datetime(month_data.iloc[:,0], format="%Y/%m/%d %H:%M:%S")
    month_data.dropna(axis=0, how='any')
    month_data=month_data.loc[(month_data.iloc[:,0].dt.year == parser.year) & (month_data.iloc[:,0].dt.month == int(month))]
    days = max(month_data.iloc[:,0].dt.day)
    return days
