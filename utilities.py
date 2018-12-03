from graphlet import *
from layout import draw
from layout2 import draw2
from layout3 import draw3
from knn import knn
import numpy as np
import os, sys
import matplotlib.pyplot as plt

# func create_matrix: input are (int(number of vertices),int(number of edges)), output is nd-array(matrix)
# func RW: input is nd-array(matrix), output is 1d-array(graphlet frequency)
# func knn: input are (nd-array(train graphlet frequencies), 1d-array(test graphlet frequency)),
#           output is the nearest neighbour's idx
# function draw: input are (nd-array(matrix),str(figure name))


def training():
    features = []
    for i in range(10000):
      # create a matrix
      matrix = create_matrix(100, 100)
    
      # calculate graphlet frequency
      features.append(RW(matrix))
      np.save('matrices/synthetic'+str(i), matrix)
      print(i)
    np.save('train_features', features)

def test():
    features = np.load('train_features.npy')
    
    # create test matrix
    test_matrix = create_matrix(100, 100)
    
    # train knn model
    idx = knn(features, RW(test_matrix))

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title("fruchterman_reingold")

    # draw
    draw(np.load('matrices/synthetic'+str(idx)+'.npy'), 'estimated_layout', False, ax)
    draw(test_matrix, 'real_layout', True, ax)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title("Kamada-Kawai")
    
    # draw
    draw2(np.load('matrices/synthetic'+str(idx)+'.npy'), 'estimated_layout2', False, ax)
    draw2(test_matrix, 'real_layout2', True, ax)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title("Spectral method with Laplacian matrix")
    
    # draw
    draw3(np.load('matrices/synthetic'+str(idx)+'.npy'), 'estimated_layout3', False, ax)
    draw3(test_matrix, 'real_layout3', True, ax)

def clear():
    array = np.ones((100,100))*0
    draw(array, 'estimated_layout', False, None)
    draw(array, 'real_layout', True, None)
