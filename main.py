"""
Created on Wed Nov 24 10:19:00 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti 
          Vadilonga00 : Francesca Vadilonga
"""

import Utils
import time
from queue import Queue 
from StatsExtractor import StatsExtractor
from Result import Result

if __name__ == '__main__':
    
    start = time.time()
    
    parser = Utils.initializeParser()
    result = Result()

    fileList = Utils.get_files_list(parser)
    queue = Queue()

    for f in fileList:
        statsExtractor = StatsExtractor(queue)
        statsExtractor.start()
        queue.put((parser, f, fileList[f], result))

    queue.join()

# TODO add graph generation for every borough
# =============================================================================
# mean_trip_per_borough, borough_data = stats.stats_per_borough(parser, month_data, giorni_del_mese)
# histogram,pie = stats.grafica_mese(mean_trip_per_borough)
# =============================================================================
    end = time.time()
    print(f'Task executed in : {end-start} s')
