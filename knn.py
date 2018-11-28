import numpy as np


def knn(features, test_feature):
    features = np.array(features)
    features = np.log(features/np.sum(features, axis=1).reshape(features.shape[0],1)+1e-10)
    test_feature = np.array(test_feature)
    test_feature = np.log(test_feature/np.sum(test_feature)+1e-10)
    idx = np.argmin(np.sum((features - test_feature)**2, axis=1))
    return idx
