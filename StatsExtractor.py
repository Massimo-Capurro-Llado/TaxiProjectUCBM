"""
Created on Wed Dec  8 15:37:55 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti
          Vadilonga00 : Francesca Vadilonga
"""

from threading import Thread
import Utils
import pandas as pd


class StatsExtractor(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    # Every thread will load a month_dataframe and get for every borough the average daily trips for the month and put
    # the result into a dictionary Todo: Use a dataframe for the result

    def run(self):
        parser, month, file, result = self.queue.get()
        print('Thread started')
        month_data = Utils.read_csv(file, parser.zone)
        month_data['tpep_pickup_datetime'] = pd.to_datetime(month_data['tpep_pickup_datetime'], format="%Y/%m/%d %H:%M:%S")
        days = max(month_data['tpep_pickup_datetime'].dt.day)

        mean_borough_trips = {}
        for i in parser.borough:
            mean_borough_trips[i] = {month: round(month_data[month_data['Borough'] == i].shape[0] / days)}
        result.add_results(mean_borough_trips)
        self.queue.task_done()
