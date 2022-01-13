# TaxiProject
Code that analyzes the average number of daily taxi trips in new york according to certain inputs. 


# Index

- [How to get started](#how-to-get-started)
- [How to contribute](#how-to-contribute)

# How to get started

## Before Execution
Before launching the program you must:


  -Put the data sets inside the 'indata' folder, otherwise specify the path of the directory with the -i1 option.
  For example if you put files in the folder 'source' you must execute: python3 main.py 2021 -i1 ./source
  
  
  -Put taxi+_zone_lookup.csv inside the 'zone_lookup' folder, otherwise specify the file path with the -i3 option.
  For example if you put files in the folder 'source2' you must execute: python3 main.py 2021 -i3 source2/taxi+_zone_lookup.csv
  
  
  -Report results will be automatically saved to folder 'outdata',
  if you want to save them in another folder you can specify it with the -i5 option.
  For example if you want to save report results in the folder 'result' you must execute: python3 main.py -i5 ./result
## To execute
To execute the script you must:

   -Insert the year field which is mandatory
   
   
    Example of execution commands: python3 main.py 2021
    
    
    In this way you will get a full year analysis in each borough
    
To analyze only a few desired months or boroughs (optional):


    -This command perform the analysis to the specified year, with specified months including all boroughs.
    
    python3 main.py 2021 -i2 3 6 9 12
    
    
    -This command perform the analysis to the specified year, with specified boroughs including all months.
    
    python3 main.py 2021 -i4 Manhattan Queens Staten Island
    
    
    -This command perform the analysis to the specified year, with specified months and boroughs.
    
    python3 main.py 2021 -i2 3 6 9 12 -i4 Manhattan Queens Staten Island 
    
# How to contribute

## Project structure
The project is structured as follows:

   -main.py  -> contains the main script to execute.
   
   -indata and zone_lookup  -> contains file used to obtain the report unless otherwise indicated in execution
   
   -outdata  ->  contains the report's result unless otherwise indicated in execution

# Authors
Code written by:

Capurro Llado Massimo, Carpineti Francesco, Vadilonga Francesca
