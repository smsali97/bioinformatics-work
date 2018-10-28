'''
Created on Apr 30, 2018

Burrows Wheel Transform

@author: Sualeh Ali
'''
import numpy as np
import pandas as pd

def main():
    text = "ABRACADABRA!"
    text2 = transform("ABRACADABRA!")
    print(inverseTransform(text2))

def transform(text):
    '''' Takes a string text and computes its BWT '''
    df = pd.DataFrame()
    chars = np.array(list([c for c in text]))
    for i in range(len(text)):
        df[i] = np.roll(chars, -i)
    df = df.sort_values([i for i in range(len(text))])
    word = ""
    for value in df.iloc[:,-1]:
        word += value
    return word

def inverseTransform(transform):
    ''' returns the original text from the BWT(text) '''
    n = len(transform) - 1
    df = pd.DataFrame(columns=[i for i in range(n+1)])
    df[0] = pd.Series(sorted(list(transform)))
    df[n] = pd.Series(list(transform))
    
    # 0 1 2 3
    # 3 0 
    # 3 0 1
    # 3 0 1 2
    cols = [n]
    for i in range(1,n):
        cols.append(i-1)
        # chop off till the i-th approach and attach it to the end?
        new_data = pd.Series(np.array(df.sort_values(cols).iloc[:,i-1]))
        df[i] = new_data
    text = ""
    arr = df.iloc[0]
    for i in range(1,n+1):
        text += arr[i] + ""
    text += arr[0] 
    return text

if __name__ == '__main__':
    main()