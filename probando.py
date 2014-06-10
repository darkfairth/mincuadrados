
from numpy import *


def mult(matriz1,matriz2):
    if matriz1[0].size != matriz2.shape[0]:
        return ("Dimensiones incorrectas")
    else:
        nmatriz = zeros((matriz1.shape[0],matriz2[0].size))
        for i in range(matriz1.shape[0]):
            for j in range(matriz2[0].size):
                for k in range(matriz2.shape[0]):
                    nmatriz[i][j]+= matriz1[i][k]*matriz2[k][j]
        return nmatriz
