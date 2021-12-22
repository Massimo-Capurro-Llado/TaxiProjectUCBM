# TaxiProject
Code that analyzes the average number of daily taxi trips in new york according to certain inputs. 


# Index

- [How to get started](#how-to-get-started)
- [How to contribute](#how-to-contribute)

# How to get started

## Before Execution
Before launching the program you must:


  -Put the data sets inside the 'indata' folder, otherwise specify the path with the -i1 option.
  
  
  -Put taxi+_zone_lookup.csv inside the 'Specifiche' folder.
## To execute
To execute the script you must:

   -Insert the year field which is mandatory
   
   
    Examples of execution commands: python3 main.py 2021
    
    
    In this way you will get a full year analysis in each borough
    
To analyze only a few desired months or boroughs (optional):


    -This command perform the analysis to the specified year, with specified months including all boroughs.
    
    python3 main.py 2021 -i2 [3, 6, 9, 12]
    
    
    -This command perform the analysis to the specified year, with specified boroughs including all months.
    
    python3 main.py 2021 -i5 ['Manhattan', 'Queens', 'Staten Island']
    
    
    -This command perform the analysis to the specified year, with specified months and boroughs.
    
    python3 main.py 2021 -i2 [3, 6, 9, 12] -i5 ['Manhattan', 'Queens', 'Staten Island'] 
    
# How to contribute

## Project structure

# Authors
Code written by:

Capurro Llado Massimo, Carpineti Francesco, Vadilonga Francesca
