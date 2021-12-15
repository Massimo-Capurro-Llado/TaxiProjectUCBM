"""
Created on Wed Dec  8 15:37:55 2021

@authors: Massimo-Capurro-Llado : Massimo Capurro Llado
          francescocarpineti091299 : Francesco Carpineti
          Vadilonga00 : Francesca Vadilonga
"""

from threading import Lock

class Result:

    def __init__(self):

        self.result = {}
        self.lock = Lock()


    def add_results(self, thread_result):
        self.lock.acquire()
        for borough in thread_result:
            if borough in self.result:
                for month in thread_result[borough]:
                    self.result[borough][month] = thread_result[borough][month]
            else:
                self.result[borough] = thread_result[borough]

        self.lock.release()