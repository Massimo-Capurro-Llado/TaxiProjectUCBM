"""
Created on Wed Nov 24 10:19:00 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti 
          Vadilonga00 : Francesca Vadilonga
"""
import Utils
import time
import stats 

start = time.time()

parser= Utils.initializeParser()

result, period, result_borough= stats.statistics(parser)


end = time.time()
print(end - start)
