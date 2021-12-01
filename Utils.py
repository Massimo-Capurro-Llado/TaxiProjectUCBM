
"""
Created on Wed Nov 24 11:06:08 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti 
          Vadilonga00 : Francesca Vadilonga
"""

import pandas as pd
import sys

#Function to read only desired columns of CSV file
def ReadCSVFile(file, columns):
    try:
        csvfile= open(file)
        data = pd.read_csv(csvfile, usecols=columns)
        return data
    except OSError as e:
        print(e)
        sys.exit()