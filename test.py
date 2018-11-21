from graphlet import *
from layout import draw
from knn import knn

# func create_matrix: input are (int(number of vertices),int(number of edges)), output is nd-array(matrix)
# func RW: input is nd-array(matrix), output is 1d-array(graphlet frequency)
# func knn: input are (nd-array(train graphlet frequencies), 1d-array(test graphlet frequency)),
#           output is the nearest neighbour's idx
# function draw: input are (nd-array(matrix),str(figure name))


features = []
for i in range(1000):
    # create a matrix
    matrix = create_matrix(100, 100)

    # calculate graphlet frequency
    features.append(RW(matrix))
    np.save('matrices/synthetic'+str(i), matrix)
    print(i)
np.save('train_features', features)

# create test matrix
test_matrix = create_matrix(100, 100)

# train knn model
idx = knn(features, RW(test_matrix))

# show and save the real and estimated layouts
draw(np.load('matrices/synthetic'+str(idx)+'.npy'), 'estimated_layout')
draw(test_matrix, 'real_layout')