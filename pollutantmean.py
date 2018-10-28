'''
Created on Apr 17, 2018

@author: Sualeh Ali
'''
import csv

def main():
    directory = "F:/Drive/Books/Bioinformatics/assignments"
    pollutant = "sulfate"
    id = range(1,11)
    pollutantmean(directory, pollutant, id)


"""
Calculates the mean of a pollutant (sulfate or nitrate)
across a specified list of monitors. The function ‘pollutantmean’ takes three arguments: ‘directory’,
‘pollutant’, and ‘id’. Given a vector monitor ID numbers, ‘pollutantmean’ reads that monitor’s
particulate matter data from the directory specified in the ‘directory’ argument and returns the mean
of the pollutant across all of the monitors, ignoring any missing values coded as NA
"""
def pollutantmean(directory, pollutant, id=range(1,333)):
    # counter
    ctr = 0
    # cumulative c_sum
    c_sum = 0
    for i in id:
        # Each csv files
        with open(directory + "/{0:03}.csv".format(i), newline='') as csvfile:
            
            reader = csv.reader(csvfile, delimiter='\n')
            next(reader)
            for row in reader:
                items = row[0].split(",")
                # if not empty
                if pollutant == 'sulfate' and not items[1] == 'NA':
                    c_sum += float(items[1])
                    ctr += 1
                elif pollutant == 'nitrate'and not items[2] == 'NA':
                    c_sum += float(items[2])
                    ctr += 1
    print("{:.3f}".format(c_sum/ctr))        
                

if __name__ == '__main__':
    main()