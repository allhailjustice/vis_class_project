# ProcessBook

Up to now, we have 4 .py files in this folder.
* graphlet.py: calculate graphlet frequency by random walk
* layout.py: draw the layout
* knn.py: train a nearest neighbour model
* test.py: Show how to use the files above
* interface.py: Show a interface for user interaction

Please refer to interface.py for usage

## Overview and Motivation
* Graph is often used to abstract data. In many research fields, the problem of data analysis can be transformed into graph analysis that focuses on the topological structure of graph. One of the important parts of this project is to measure the topological similarity between graphs, which is exact what we are interested in.
* This project combines visualization and machine learning. It works on predicting visualiztion performance on specific layouts for graph, using machine learning strategy. By doing this project, we may get further inspriation on how to apply machine learning approaches to visualization.
* So far, the ways we have learnt in class to evaluate visualization layouts are more like intuitive senses rather than numerical metrics. However, the latter one can lead to automatic evaluation process withou human inspection, which is very convenient for the cases have large amount of graphs. This project uses several aesthetic criteria and metrics to evaluate visualization performance which can be a supplement for the course.

## Related Work
* transactions on visualization and computer graphics, 24(1), 478-488. Kwon, O. H., Crnovrsanin, T., & Ma, K. L. (2018). What Would a Graph Look Like in This Layout? A Machine Learning Approach to Large Graph Visualization. IEEE
* real data: https://github.com/shiruipan/graph_datasets.

## Questions
What questions are you trying to answer? How did these questions evolve over the course of the project? What new questions did you consider in the course of your analysis?

## Data
Source, scraping method, cleanup, etc.

## Implementation

### part 1: graphlet kernel

### part 2: interface
Start the interface:
![Image text](https://github.com/allhailjustice/vis_class_project/blob/master/screenshots/Screen%20Shot%202018-12-11%20at%209.00.44%20PM.png)
The interface has three buttons:
* Training:
* Test:
* Clear:
and two rows of plots:
* Estimated layout:
* Real layout:

Run a test:
![Image text](https://github.com/allhailjustice/vis_class_project/blob/master/screenshots/Screen%20Shot%202018-12-11%20at%209.01.24%20PM.png)

## Visualization Technique
What were the difficulties in implementing the paper? What did you have to learn, above and beyond the paper, in order to implement it?

## Evaluation
What did you choose to evaluate the technique? Did you follow the experimental setup as described by the paper, or did you pursue a different form of evaluation?

## Analysis
What did you learn about the technique by applying it to the different datasets? How can you characterize the technique’s strengths and weaknesses in terms of the data?
