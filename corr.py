'''
Created on Apr 17, 2018

@author: Sualeh Ali
'''
import complete
import numpy as np
import csv

def main():
    directory = "F:/Drive/Books/Bioinformatics/assignments"
    directory2 = "F:/Drive/Books/Bioinformatics/assignments/specdata"
    threshold = 150
    print(corr(directory2, threshold)[:6])

"""
This function that takes a directory of data files and a threshold for complete cases and calculates the
correlation between sulfate and nitrate for monitor locations where the number of completely observed cases
(on all variables) is greater than the threshold. The function should return a vector of correlations for the
monitors that meet the threshold requirement. If no monitors meet the threshold requirement, then the
function should return a numeric vector of length 0. A prototype of this function follows
"""
def corr(directory, threshold):
    
    df = complete.complete(directory, [i for i in range(1,333)])
    # keeping track whether threshold has crossed or not
    
    id_list = df[df.nobs > threshold].id
    corr_list = []
    for i in id_list:
        with open(directory + "/{0:03}.csv".format(i), newline='') as csvfile:
            
            reader = csv.reader(csvfile, delimiter='\n')
            # skip header file
            next(reader)
            
            sulfate_list = []
            nitrate_list = []

            
            for row in reader:
                items = row[0].split(",")
                
                if not items[1] == "NA" and not items[2] == "NA":
                    sulfate_list.append(float(items[1]))
                    nitrate_list.append(float(items[2]))
            val = round(np.corrcoef(sulfate_list, nitrate_list)[0][1],5)
            corr_list.append(val)
    return corr_list

if __name__ == '__main__':
    main()