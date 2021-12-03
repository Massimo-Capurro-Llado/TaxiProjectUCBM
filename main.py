"""
Created on Wed Nov 24 10:19:00 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti 
          Vadilonga00 : Francesca Vadilonga
"""
import Utils
import pandas as pd
#import multiprocessing as mp
import time
import readglob as rg

start = time.time()

#Constanti
taxi_cols=['tpep_pickup_datetime', 'PULocationID']
zone_cols=['LocationID', 'Borough']
parser= Utils.initializeParser()
big_frame = rg.read_multiple_file(parser)
l = Utils.ViaggiPerGiorno(big_frame, parser)
periodo = Utils.periodopiùfrequente(l)
end = time.time()
print(end - start)
