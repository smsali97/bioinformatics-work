'''
Created on Apr 17, 2018

@author: AC
'''

import csv
import pandas as pd


def main():
    directory = "F:/Drive/Books/Bioinformatics/assignments"
    id = [2, 4, 8, 10, 12]
    print(complete(directory,id))

"""
This function reads a directory full of files and reports the number of completely observed cases in
each data file. The function should return a data frame where the first column is the name of the file and
the second column is the number of complete cases.
"""
def complete(directory, id):
    stuff = pd.DataFrame(columns=["id","nobs"])
    nobs_list = []
    for i in id:
        nobs = 0
        # Each csv file
        with open(directory + "/{0:03}.csv".format(i), newline='') as csvfile:
            
            reader = csv.reader(csvfile, delimiter='\n')
            next(reader)
            for row in reader:
                items = row[0].split(",")
                # Check if not empty
                if not (items[1] == "NA" or items[2] == "NA"): nobs += 1
        nobs_list.append(nobs)
    stuff = pd.DataFrame({"id":id,"nobs":nobs_list},[i for i in range(1,len(id)+1)])               
    return stuff              


if __name__ == '__main__':
    main()
