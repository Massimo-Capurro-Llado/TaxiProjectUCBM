"""
Created on Wed Dec  8 15:37:55 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti
          Vadilonga00 : Francesca Vadilonga
"""

from threading import Thread
import Utils


class StatsExtractor(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        parser, month, file, result = self.queue.get()
        month_data = Utils.read_csv(file, parser.zone)
        days = Utils.data_cleaner(month_data, parser, month)
        mean_borough_trips = {}
        for i in parser.borough:
            mean_borough_trips[i] = {month: round(month_data[month_data['Borough'] == i].shape[0] / days)}
        result.add_results(mean_borough_trips)
        self.queue.task_done()

