#!/usr/bin/python

import random
import os

import ConfigParser

import time

config = ConfigParser.RawConfigParser()
config.read('math.ini')

previousRand = 0
randBytes = bytearray(os.urandom(32*1024))
randByteIter = 0
iterationsLimit = 250
workFieldCounter = 0

multiplyArray = [[0 for j in range(10)] for i in range(10)]
divisionArray = [[0 for j in range(10)] for i in range(10)]

logFileName = "math.log"
logFile = 0

def log(logMessage):
    logFile.write("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + "] " + logMessage + "\n")

def getRandom():
    global randByteIter

    a = randBytes[randByteIter]
    randByteIter += 1

    return a 



def getRandomInLimits(min, max):
    global previousRand
    global randByteIter
    iterations = 0
    
    #log("getRandomInLimits("+str(min)+", "+str(max)+")")

    while True and iterations < iterationsLimit :
        iterations += 1
        #a = ord(os.urandom(1))
        a = randBytes[randByteIter]
        randByteIter += 1
        if ( a >= min and a < max and a != previousRand ) :
            break

    previousRand = a
    return previousRand



def generateWorkCell(op1, oper, op2, result, cellIdx):
    print "<td class=\"workcell\" id=\"%d\">%d&nbsp;%s&nbsp;%d&nbsp;=&nbsp;<input name=\"rezuser_%d\" class=\"rezuser\" type=\"text\"/><input  name=\"rezcomp_%d\" type=\"hidden\" value=\"%d\"><input  name=\"challenge_%d\" type=\"hidden\" value=\"%d%s%d\"></td></td><td class=\"sepcell\"></td>" % (cellIdx, op1, oper, op2, cellIdx, cellIdx, result, cellIdx, op1, oper, op2)



def multiplication(workFieldCounter) :
    global multiplyArray
    iterations_1 = 0

    iterBreak1 = True
    iterBreak2 = True
    
    while iterBreak1 and iterations_1 < iterationsLimit :
        a = getRandom()%10

        mSelectionSetString = "math.multiply." + str(a)

        if config.get("Multiplication", mSelectionSetString) == "on" :

            iterations_2 = 0

            while iterBreak2 and iterations_2 < iterationsLimit :

                if sum(multiplyArray[a]) == 10 :
                    multiplyArray[a] = [0 for i in range(10)]

                b = getRandom()%10
                
                if  multiplyArray[a][b] == 0 :
                    multiplyArray[a][b] = 1
                    iterBreak2 = False

                iterations_2 = iterations_2 + 1
                
            generateWorkCell(a+1, 'x', b%10, (a+1)*(b%10), workFieldCounter)
            iterBreak1 = False

        iterations_1 = iterations_1 + 1

    if iterBreak1 :
        print "<td class=\"workcell\" id=\"",workFieldCounter,"\">u&nbsp;x&nbsp;x&nbsp;=</td></td><td class=\"sepcell\"></td>"



def division(workFieldCounter) :
    global divisionArray
    iterations_1 = 0

    iterBreak1 = True
    iterBreak2 = True
    
    while iterBreak1 and iterations_1 < iterationsLimit :
        a = getRandom()%10

        mSelectionSetString = "math.division." + str(a)

        if config.get("Division", mSelectionSetString) == "on" :

            iterations_2 = 0

            while iterBreak2 and iterations_2 < iterationsLimit :

                if sum(divisionArray[a]) == 10 :
                    divisionArray[a] = [0 for i in range(10)]

                b = getRandom()%10
                
                if  divisionArray[a][b] == 0 :
                    divisionArray[a][b] = 1
                    iterBreak2 = False

                iterations_2 = iterations_2 + 1
                
            generateWorkCell((a+1)*b, ':', a+1, b, workFieldCounter)
            iterBreak1 = False

        iterations_1 = iterations_1 + 1

    if iterBreak1 :
        print "<td class=\"workcell\">u&nbsp;:&nbsp;x&nbsp;=</td></td><td class=\"sepcell\"></td>"



def addition(max, min, workFieldCounter):
    a = getRandomInLimits(min, max)
    b = getRandomInLimits(min -1, max - a)

    generateWorkCell(a, '+', b, a+b, workFieldCounter)



def substraction(max, min, workFieldCounter):    
    a = getRandomInLimits(min, max)
    b = getRandomInLimits(min, max)

    if a > b :
        generateWorkCell(a, '-', b, a-b, workFieldCounter)
    else :
        generateWorkCell(b, '-', a, b-a, workFieldCounter)



def _disabled_substraction(max, min, workFieldCounter):
    log("substraction("+str(max)+", "+str(min)+", "+str(workFieldCounter)+")")
    a = getRandomInLimits(max/2, max)
    b_tail = getRandomInLimits(a%100 + 1, 100)
    b_head = getRandomInLimits(0, a/100)
    b = b_head*100 + b_tail
    
    generateWorkCell(a, '-', b, a-b, workFieldCounter)
    

logFile = open(logFileName, "a")
log("Logfile open")    

print "Content-type: text/html\n\n"
print "<html><script src=\"/schooldoc/jquery-3.2.1.min.js\"></script><script src=\"/schooldoc/math.js\"></script><link rel=\"stylesheet\" type=\"text/css\" href=\"/schooldoc/math.css\"><style>.sep_cell {width: 60px;height: %dpx;}</style><body><form action=\"/schoolsrc/sendRez.py\" method=\"post\"><table border='0'>" % int(config.get("Main", "math.main.space.vertical"))

for rows in range(0, int(config.get("Main", "math.main.rows"))):
    print "<tr>"

    for cols in range(0, int(config.get("Main", "math.main.columns"))):
        workFieldCounter+=1

        randChoise = getRandomInLimits(0, 100)

        if randChoise < int(config.get("Addition", "math.addition.weight")) :
            addition(int(config.get("Addition", "math.addition.max")), 100, workFieldCounter)
        else :
            if randChoise < int(config.get("Addition", "math.addition.weight")) + int(config.get("Substraction", "math.substraction.weight")) :
                substraction(int(config.get("Substraction", "math.substraction.max")), 100, workFieldCounter)
            else:
                if randChoise < int(config.get("Addition", "math.addition.weight")) + int(config.get("Substraction", "math.substraction.weight")) + int(config.get("Multiplication", "math.multiply.weight")) :
                    multiplication(workFieldCounter)
                else:
                    division(workFieldCounter)
                    
    print "</tr><tr><td class=\"seprow\"></td></tr>"

print "</table></form>"
#print "<a href=\"/schoolscr/load_setup.py\">Setup</a>"
print "<input type=\"button\" name=\"check\" value=\"Klaar\" onclick=\"checkComplete()\"/>"
print "</body></html>"

log("Logfile close")
close(logFile)
