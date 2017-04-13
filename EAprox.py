import numpy as np
from math import fabs
import matplotlib.pyplot as plt
from numpy import linalg as LA



def GregsCircles(matrix):
    if isSquare(matrix) != True:
        print('Your input matrix is not square!')
        return []
    circles = []
    for x in range(0,len(matrix)):
        radius = 0
        piv = matrix[x][x]
        for y in range(0,len(matrix)):
            if x != y:
                radius += fabs(matrix[x][y])
        circles.append([piv,radius])
    return circles

def plotCircles(circles):
    index, radi = zip(*circles)
    Xupper = max(index) + np.std(index)
    Xlower = min(index) - np.std(index)
    Ylimit = max(radi) + np.std(index)
    fig, ax = plt.subplots() 
    ax = plt.gca()
    ax.cla()
    ax.set_xlim((Xlower,Xupper))
    ax.set_ylim((-Ylimit,Ylimit))
    plt.xlabel('Real Axis')
    plt.ylabel('Imaginary Axis')
    plt.title('Gershgorin circles')
    for x in range(0,len(circles)):
        circ = plt.Circle((index[x],0), radius = radi[x])
        ax.add_artist(circ)
    ax.plot([Xlower,Xupper],[0,0],'k--')
    ax.plot([0,0],[-Ylimit,Ylimit],'k--')
    fig.savefig('plotcircles.png')
    
def isSquare(m):
    cols = len(m)
    for row in m:
        if len(row) != cols:
            return False
    return True

def main():
    test = np.array([[10,-1,0,1],[0.2,8,0.2,0.2],[1,1,2,1],[-1,-1,-1,-11]])
    temp = GregsCircles(test)
    plotCircles(temp)

if __name__ == '__main__':
    main()