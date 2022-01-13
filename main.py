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
from datetime import datetime


def stats_extractor(file_list):
    queue = Queue()
    for f in file_list:
        extractor = StatsExtractor(queue)
        extractor.start()
        queue.put((parser, f, file_list[f], result))
    queue.join()


if __name__ == '__main__':
    """
            Main execution. This code performs the following actions: 
             - Initialize the parser
             - Extract user's input as parameters specification for the current analysis
             - Generate the list of files that have to be analyzed
             - Perform the analysis (using threads)
             - Generate a global report and a partial report for every month (.xlsx files)
             - Generate a graph for every month (.png files)
    """

    start = time.time()
    print(f"Starting the analysis at: {datetime.fromtimestamp(start)}\n")

    parser = Utils.initialize_parser()
    result = Result()

    file_list = Utils.get_files_list(parser)
    stats_extractor(file_list)
    Utils.generate_graphs(result.result, parser)
    Utils.save_excel_file(parser, result.result)
    end = time.time()
    print(f'Task executed in : {end - start} s')
