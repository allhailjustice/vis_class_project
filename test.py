from graphlet import *
from layout import draw
from knn import knn
from utilities import training
# func create_matrix: input are (int(number of vertices),int(number of edges)), output is nd-array(matrix)
# func RW: input is nd-array(matrix), output is 1d-array(graphlet frequency)
# func knn: input are (nd-array(train graphlet frequencies), 1d-array(test graphlet frequency)),
#           output is the nearest neighbour's idx
# function draw: input are (nd-array(matrix),str(figure name))

training()

features = np.load('train_features.npy')

# create test matrix
test_matrix = create_matrix(100, 100)

# train knn model
idx = knn(features, RW(test_matrix))

# show and save the real and estimated layouts
draw(np.load('matrices/synthetic'+str(idx)+'.npy'), 'estimated_layout', False, None)
draw(test_matrix, 'real_layout', True, None)
