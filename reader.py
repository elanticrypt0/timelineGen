import csv
from source import Source
from event import Event

def get_source(sources,source_file):
    
    with open(source_file,newline='') as csvfile:
        datareader = csv.reader(csvfile,delimiter=',',quotechar='|')
        for row in datareader:
            sources.append(Event(row[0],row[1],row[2],row[3]))
            