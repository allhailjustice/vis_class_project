from graphlet import *
from layout import draw
from knn import knn

# features = []
# for i in range(1000):
#     matrix = create_matrix(100, 100)
#     features.append(RW(matrix))
#     np.save('matrices/synthetic'+str(i), matrix)
#     print(i)
# np.save('train_features', features)
features = np.load('train_features.npy')
test_matrix = create_matrix(100, 100)
idx = knn(features, RW(test_matrix))
print(idx)
draw(np.load('matrices/synthetic'+str(idx)+'.npy'), 'estimated_layout')
draw(test_matrix, 'real_layout')