# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:43:31 2021

@author: francescocarpineti091299 : Francesco Carpineti
         Massimo-Capurro-Llado : Massimo Capurro Llado
         Vadilonga00 : Francesca Vadilonga
"""

import Utils
import pandas as pd
import matplotlib as plt

# TODO: Implement threading to plot the graphs. This file as it is has no use and so is not called in the main

def create_graphs(mean_trip_per_borough):
    # histogram
       histogram = plt.bar(mean_trip_per_borough.keys(), mean_trip_per_borough.values(), color='g')
    # Pie
       plt.figure(figsize=(15,15))
       plt.style.use('ggplot')
       labels = []
       sizes = []
       explode= (.4, .12, .12, .12, .0, .12)
       for x, y in mean_trip_per_borough.items():
            labels.append(x)
            sizes.append(y)
       # Plot
       pie=plt.pie(sizes, labels=labels, explode=explode, pctdistance=0.20, autopct='%.2f %%')
       plt.legend(title="Borough:")

       return histogram, pie