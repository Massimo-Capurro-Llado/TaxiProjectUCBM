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

#result, period, result_borough= stats.statistics(parser)
month_data, giorni_del_mese = stats.statistics_per_month(parser)
mean_trip_per_borough, borough_data = stats.stats_per_borough(parser, month_data, giorni_del_mese)
histogram,pie = stats.grafica_mese(mean_trip_per_borough)
end = time.time()
print(end - start)

