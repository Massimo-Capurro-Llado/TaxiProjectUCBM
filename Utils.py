
"""
Created on Wed Nov 24 11:06:08 2021

@author: massi
"""

import pandas as pd
import sys

def ReadCSVFile(file):
    try:
        csvfile= open(file)
        data = pd.read_csv(csvfile)
        return data
    except OSError as e:
        print(e)
        sys.exit()
    