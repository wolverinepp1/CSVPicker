#!/usr/bin/python
import csv
import os
import sys
import datetime

inputFolderCider = 'input/cider'
inputFoldertcDetector = 'input/tcDetector'
outputFolderMerged = 'output/merged'
outputFolderMergedFile = 'output/merged/merged.csv'


def readLineFromCSV( str, num ):
    "This function is to read a csv file"
    with open(str , newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        lineNumber = 1
        for row in spamreader:
            if lineNumber == num:
                return row;
                # print(', '.join(row))
            else:
                lineNumber += 1

def readCsv( str ):
    with open(str, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        rows = ''
        for row in spamreader:
            rows += (';'.join(row))+'\n'
            # print(rows)
    return rows

def compareSN( sn1, sn2):
    if sn1 == sn2:
        return 1;
    else:
        return 0;

def writeFile(inputFile, outFile):
    with open(outFile, 'w') as src:
        src.write(inputFile)

def batchProcess(outputCSV):
    concatenationCsv(inputFolderCider, outputFolderMerged)
    with open(outputFolderMergedFile, newline='') as csvsrc:
        srcReader = csv.reader(csvsrc, delimiter=';', quotechar='|')
        strToCsvOut = '';
        for row in srcReader:
            rowToWrite = row
            with open(inputFoldertcDetector + '/' + os.listdir(inputFoldertcDetector)[0], newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                for line in spamreader:
                    if compareSN(line[0], row[0]):
                        del rowToWrite[2]
                        rowToWrite.insert(2, '=\"NON COLLECTANT\"')
                        break;
            strToCsvOut += ';'.join(rowToWrite) + '\n'
        writeFile(strToCsvOut, 'output/' + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '_' + outputCSV)



# def writeLineToCSV()

def concatenationCsv( inputFolder, outputFolder ):
    merged = ''
    for file in os.listdir(inputFolder):
        merged += readCsv(inputFolder + '/'+ file)
    writeFile(merged, outputFolderMergedFile)



if __name__ == '__main__':
    batchProcess('result.csv')
    os.remove(outputFolderMergedFile)