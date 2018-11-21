import numpy as np
m = np.load('test.npy')
A = []
B = []
for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j] == 1:
            A.append(str(i))
            B.append(str(j))

# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# Build a dataframe with your connections

df = pd.DataFrame({ 'from':A, 'to':B})
df

# Build your graph
G=nx.from_pandas_edgelist(df, source='from', target='to')
# Fruchterman Reingold
nx.draw(G, with_labels=True, node_size=100, node_color="skyblue", pos=nx.fruchterman_reingold_layout(G))
plt.title("fruchterman_reingold")
