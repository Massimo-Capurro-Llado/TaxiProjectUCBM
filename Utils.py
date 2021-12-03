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
                        default=['Manhattan'])
    
    parser.add_argument("-e", "--extension",
                        help="Input file extension, including dot (Es -> .csv)",
                        type=str,
                        default='.csv')
    
    return parser.parse_args()


#Function to read only desired columns of CSV file

def readCSVFile(file, columns):
    try:
        csvfile= open(file)
        data = pd.read_csv(csvfile, usecols=columns)
        return data
    except OSError as e:
        print(e)
        sys.exit()
