# Processbook

Main files in this folder.
* graphlet.py: calculate graphlet frequency by random walk
* layout.py: draw the layout
* knn.py: train a nearest neighbour model
* interface.py: show a interface for user interaction
* experiment_real_data.ipynb: the experiment process on real data

Please refer to interface.py for usage

## Overview and Motivation
* Graph is often used to abstract data. In many research fields, the problem of data analysis can be transformed into graph analysis that focuses on the topological structure of graph. One of the important parts of this project is to measure the topological similarity between graphs, which is exact what we are interested in.
* This project combines visualization and machine learning. It works on predicting visualiztion performance on specific layouts for graph, using machine learning strategy. By doing this project, we may get further inspriation on how to apply machine learning approaches to visualization.

## Related Work
* Oh-Hyun Kwon, Tarik Crnovrsanin, and Kwan-Liu Ma. What would a graph look like in this layout? a machine learning approach to large graph visualization. IEEE transactions on visualization and computer graphics, 24(1):478– 488, 2018. 
* Xiaowei Chen, Yongkun Li, Pinghui Wang, and John Lui. A general framework for estimating graphlet statistics via random walk. Proceedings of the VLDB Endowment, 10(3):253–264, 2016.
* Timothy A Davis and Yifan Hu. The university of florida sparse matrix collec- tion. ACM Transactions on Mathematical Software (TOMS), 38(1):1, 2011.

## Questions
In appearance, what we did is to predict the layout without computing it. However, the core question hiding behind is can we represent a layout by its corresponding topological features in the data. It can be further develop to another question which is can we depress the layout in its topological representation without lossing much information. Although our work is still in the appearance, it gives rise to some interesting thoughts for future researches.

## Data
We have two data sources. One is randomly generated synthetic dataset. The other is [SuiteSparse Matrix Collection](https://sparse.tamu.edu/) (formerly the University of Florida Sparse Matrix Collection). We extracted the symmetric matrices from it with 100-500 vertices and then did binarization.

## Implementation

### part 1: graphlet kernel
![Image text](https://github.com/allhailjustice/vis_class_project/blob/master/graphlet.PNG)

Graphlets are selected small, induced, and non-isomorphic subgraph patterns in graph. 3-node, 4-node, 5-node graphlets are shown in the figure above. Firstly, we use random walk sampling technique to compute 5-node graphlet frequency in our project. For details, please refer to [Implementation](https://github.com/allhailjustice/vis_class_project/blob/master/graphlet.py) and [Algorithm](https://arxiv.org/pdf/1603.07504.pdf). Then we do logarithmic scaling on the frequency vector and use the scaled vector as input of nearest neighbour model.

### part 2: interface

**Start the interface by running command `python3 interface.py` under the project file:**

![Image text](https://github.com/allhailjustice/vis_class_project/blob/master/screenshots/Screen%20Shot%202018-12-11%20at%209.00.44%20PM.png)

**Run a test by clicking the button `Test`, and you can test it as many times as you want by clicking `Test `:**

![Image text](https://github.com/allhailjustice/vis_class_project/blob/master/screenshots/Screen%20Shot%202018-12-11%20at%209.01.24%20PM.png)

The interface has three buttons:
* Training: It is used to re-training the dataset, it will generate ~10k connected graphs, calculate and save graphlet frequency.
* Test: It is used to test the model with an input graph and show both the estimated layouts and real layouts in three layout methods. When first run the interface, you don't need to train the data cause we've already trained it, so users can just click test to see layouts.
* Clear: It is used to clear the plots.

and two rows of plots(three plots of each):
* Estimated layout: the nearest graph's layouts from dataset selected by our graphlet kernel without computing its actual layout.
* Real layout: actual layouts computed using three layout methods.
So users can compare estimated layout with real layout multiple times in three kinds of layout methods.

## Visualization Technique
We have to get a sense on what is the graphlet and why its frequency matters. The most difficult part in this project is to implement a effective random walk algorithm to compute graphlet frequency which is introduced in another paper.

## Evaluation
We can easily evaluate the technique by visualize experiment outcome. However, we don't have method to evaluate it by some quantitative metrics.

## Analysis
The outcome of experiment on synthetic data looks good, but on real data is not good. The resason is that we use synthetic data to train our model due to insufficiency of real data, and synthetic data do not have the complex artificial features like it in real data. We all know that machine learning methods heavily rely on the quality and quatity of data. This characteristic also appear in our project. So the strength of our technique is that it works if we have appropriate training data, and weakness is that we rely too much on the training data.
