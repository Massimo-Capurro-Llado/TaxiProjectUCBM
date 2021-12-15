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


def stats_extractor(file_list):
    queue = Queue()
    for f in file_list:
        extractor = StatsExtractor(queue)
        extractor.start()
        queue.put((parser, f, file_list[f], result))
    queue.join()


if __name__ == '__main__':
    
    start = time.time()
    
    parser = Utils.initializeParser()
    result = Result()

    file_list = Utils.get_files_list(parser)
    stats_extractor(file_list)
    Utils.generate_graphs(result.result, parser)
    #TODO salva risultato in excel(Fare funzione EXCEL)
    end = time.time()
    print(f'Task executed in : {end-start} s')
