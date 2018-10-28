'''
Created on Apr 26, 2018

@author: Sualeh Ali
'''
import numpy as np


def main():
    fileName = "input.txt"
    reads = readDataFromFile(fileName)
    
    print(round(meanLength(fileName), 3))
    
    overlaps = getAllOverlaps(reads)
    prettyPrint(overlaps)

    name = findFirstRead(overlaps)
    order = findOrder(name, overlaps)
    
    genome = assembleGenome(order, reads, overlaps)
    genome2 = "TGCGAGGGAAGTGAAGTATTTGACCCTTTACCCGGAAGAGCGGGACGCTGCCCTGCGCGATTCCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGCTGGTACGTCTTCAGTAGAAAATTGTTTTTTTCTTCCAAGAGGTCGGAGTCGTGAACACATCAGT"
    print(genome)
    print(genome == genome2)
    
    
def readDataFromFile(fileName):
    ''' Reads data from file '''
    dicty = {}
    with open(fileName) as filey:
        for line in filey:
            items = line.split(" ")
            dicty[items[0]] = items[1].rstrip('\n') 
    return dicty

    
def meanLength(fileName):
    ''' Computes the mean length of all the characters in the strings '''
    return np.mean([len(value) for __, value in readDataFromFile(fileName).items()])


def getOverlap(left, right):
    ''' Takes a left and right string and computes their overlap '''
    # ABCDEF <-- left's right overlap
    # CDEFG  <-- right's left overlap

    # ABCDEF
    #  CDEFG
    # MAXIMUM OVERLAP

    # ABCDEF
    #       CDEFG
    # MINIMUM OVERLAP 

    L = min(len(left), len(right))
    
    for i in range(L):
        if left[len(left) - L + i:] == right[:L - i]:
            return left[len(left) - L + i:]
    return ""


def getAllOverlaps(reads):
    ''' Returns all the overlaps in a dict of the input file'''
    new_dict = {}
    
    for key in reads.keys():
        new_dict[key] = {}
        for key2 in reads.keys():
            if not key == key2:
                new_dict[key][key2] = len(getOverlap(reads[key], reads[key2]))
                
    return new_dict


def prettyPrint(overlaps):
    ''' Pretty prints all the overlaps in a matrix form '''
    
    keys = sorted(overlaps.keys())
    
    print("%3c " % ' ', end='')
    for key in keys:
        print("%3c " % key, end='')
    print()
    
    for key in keys:
        print("%3c " % key, end='')
        for key2 in keys:
            
            if not key == key2: print("%3d " % overlaps[key][key2], end='')
            else: print("%3c " % '_', end='')
        print("")

            
def findFirstRead(dicty):
    ''' Finds the first read that only has a significant (> 2) right end '''
    for key in dicty.keys():
        flag = True
        for key2 in dicty[key].keys():
            if dicty[key2][key] > 2: flag = False
        if flag: return str(key)
    return -1


def findKeyForLargestValue(d):
    ''' Returns the key for the largest value in the dictionary  '''
    MAX = max(d.values())
    for key, value in d.items():
        if value == MAX and value > 2: return key
    return -1


def findOrder(name, overlaps, order_list=[]):
    ''' Recursively finds the list order of the genomes with the max. overlaps '''
    order_list.append(name)
    key = findKeyForLargestValue(overlaps[name])
    if key == -1: return order_list
    else: return findOrder(key, overlaps)


def assembleGenome(readOrder, reads, overlaps):
    '''' Assembles the genome given the read order, reads, and its overlaps '''
    genome = reads[readOrder[0]]
    
    for i in range(1, len(readOrder)):
        index = overlaps[ readOrder[i - 1] ][readOrder[i]]
        genome += reads[ readOrder[i] ][index:]
    return genome

    
if __name__ == '__main__':
    main()
