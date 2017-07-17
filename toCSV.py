import os
import csv
indir = 'climateIS'

def toCSVs():
    for root, dirs, filenames in os.walk(indir):
        print("hello")
        print(filenames)
        for f in filenames:
            if f[0] != '.':
                fIn = open(os.path.join(root, f), 'r') 
                with fIn, open("outFile_" + f.replace('txt', 'csv') , 'w') as fOut:
                    o = csv.writer(fOut)
                    for line in fIn:
                        print (line)
                        o.writerow(line.split())

def toCSV(f):
    root ="~/Downloads/climateIS/" 
    fIn = open(os.path.join(root, f), 'r') 
    with fIn, open("outFile_" + f.replace('txt', 'csv') , 'w') as fOut:
        o = csv.writer(fOut)
        for line in fIn:
            print (line)
            o.writerow(line.split())

toCSV("beijing_weather.txt")

