"""
Created on Wed Nov 24 11:06:08 2021
@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti
          Vadilonga00 : Francesca Vadilonga
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
import argparse
import os
from os import path
import calendar


def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("year",
                        help="The year to put under analysis",
                        type=int)

    parser.add_argument("-i1", "--path",
                        help="Path of the directory where the files are",
                        type=str,
                        default='./indata')

    parser.add_argument("-i2", "--month",
                        help="The months to put under analysis",
                        nargs='+',
                        type=int,
                        default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    parser.add_argument("-i3", "--zone",
                        help="The zone_lookup file with information about the Borough",
                        type=str,
                        default='zone_lookup/taxi+_zone_lookup.csv')

    parser.add_argument("-i4", "--borough",
                        help="The zone_lookup file with information about the Borough",
                        type=str,
                        nargs='+',
                        default=['Manhattan', 'Queens', 'EWR', 'Bronx', 'Staten Island', 'Brooklyn'])

    parser.add_argument("-i5", "--output",
                        help="The folder for output results",
                        type=str,
                        default='./outdata')

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


def data_cleaner(month_data, parser, month):
    # take the first coloum of month_data dataframe named ['tpep_pickup_datatime']
    month_data.iloc[:, 0] = pd.to_datetime(month_data.iloc[:, 0], format="%Y/%m/%d %H:%M:%S")
    month_data.dropna(axis=0, how='any')
    month_data = month_data.loc[
        (month_data.iloc[:, 0].dt.year == parser.year) & (month_data.iloc[:, 0].dt.month == int(month))]
    days = max(month_data.iloc[:, 0].dt.day)
    return days


def generate_graphs(stats, parser):
    stats_df = pd.DataFrame(stats).sort_index()
    for i in parser.month:
        current_month = stats_df.loc[i, :]
        barplot = current_month.plot(kind='bar', title="DAILY TAXI TRIPS IN NEW YORK'S BOROUGHS", fontsize=10)
        barplot.set_xlabel("BOROUGH", fontsize=10)
        barplot.set_ylabel("AVERAGE DAILY TRIPS", fontsize=10)
        plt.tight_layout()
        plt.savefig(path.join(parser.output, f"Bar{i}_{calendar.month_name[i]}_{parser.year}.png"), dpi=300)


def save_excel_file(parser, data):
    try:
        data = pd.DataFrame(data)
        writer = pd.ExcelWriter(path.join(parser.output, f"Statistics_Global_{parser.year}.xlsx"))
        datat = data.transpose()
        datat = datat.sort_index(axis=1)
        col_names = [calendar.month_name[i] for i in datat.columns]
        datat.columns = col_names
        datat.to_excel(writer, 'GLOBAL STATS')
        writer.save()
        for i in parser.month:
            current_month = data.loc[i, :]
            writer = pd.ExcelWriter(path.join(parser.output, f"Statistics_{calendar.month_name[i]}_{parser.year}.xlsx"))
            current_month.to_excel(writer, 'MONTH STATS')
            writer.save()

    except OSError as e:
        print(e)
        sys.exit()


def create_output_directory(parser):
    out = parser.output
    exist = os.path.exists(out)

    if not exist:
        os.makedirs(out)
        print(f"Created a folder named {out} in the project folder. There you will find all your results")
