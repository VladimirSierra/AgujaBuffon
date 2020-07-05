import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import random
from math import pi,cos,sin, trunc
import numpy as np

#variables para el programa
simulaciones = 10000
agujasCortan = 0
longitudAguja = 0.75
numCeldas = 100
distanciaCeldas = 1

#funcion que genera vectores de longitud l
def vectorL(l=0.75, d=1, rendijas=10):
    x1,y1 = random.uniform(0,d*rendijas), random.uniform(0,d*rendijas)
    tetha = random.uniform(0,2*pi)
    x2,y2 = x1+l*cos(tetha), y1 + l*sin(tetha)
    return [[x1,y1],[x2,y2]]

def agujaIntersecta(x1,x2,distanciaCeldas):
    rendija1 = trunc(x1/distanciaCeldas)
    rendija2 = trunc(x2/distanciaCeldas)
    return rendija1 != rendija2

def generateFigure(simulaciones, longitudAguja, numCeldas, distanciaCeldas):
    agujasCortan = 0

    agujas = []
    for i in range(simulaciones):
        agujas.append(vectorL(longitudAguja, distanciaCeldas, numCeldas))


    linesRendijas = []
    for i in range(numCeldas+1):
        linesRendijas.append([[i*distanciaCeldas,0], [i*distanciaCeldas,numCeldas*distanciaCeldas]])
    lines2 = LineCollection(linesRendijas, linewidths=1, colors='red')

    plt.close('all')
    fig, ax = plt.subplots()
    ax.set_xlim(-longitudAguja, distanciaCeldas*numCeldas+longitudAguja)
    ax.set_ylim(-longitudAguja, distanciaCeldas*numCeldas+longitudAguja)
    lines = LineCollection(agujas, linewidths=0.5, color='blue')
    ax.add_collection(lines)
    ax.add_collection(lines2)
    ax.autoscale()

    for aguja in agujas:
        if(agujaIntersecta(aguja[0][0], aguja[1][0], distanciaCeldas)):
            agujasCortan += 1

    myPi = (2*longitudAguja*simulaciones) / (distanciaCeldas*agujasCortan)

    ax.set_title('Simulaciones: {} \nColisiones: {} \nAproximacion de pi: {} '.format(simulaciones, agujasCortan, myPi))

    return fig

def simSimplificada(repeticiones):
    d,l = 0.75, 0.25
    count = 0
    for i in range(repeticiones):
        x = random.uniform(0,d)
        y = l * cos( random.uniform(0,pi/2))
        if y > x:
            count += 1
    return ((2*l*repeticiones)/(d*count))

#Function that returns an array with diferent sizes from 100 to max
def getSizes(max=100000):
    x, n, i = [] , 100, 1
    x.append(100)
    while(n<max):
        n += (10*i)
        i += 1
        x.append(n)
    x.append(max)
    return x

def getMonteCarloImage():
    sizes = getSizes(100000)
    results = []
    for size in sizes:
        results.append(simSimplificada(size))
    sizeSample = np.array(sizes)
    values = np.array(results)

    plt.close('all')
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(sizeSample, values, linewidth=1, color='r')
    ax.axhline(y=3.141592653, color='blue', linestyle='-')
    ax.autoscale()
    return fig