import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def draw(matrix, name, close, axes):
    A, B = np.where(matrix == 1)
    A = list(A)
    B = list(B)
    df = pd.DataFrame({'from': A, 'to': B})
    G = nx.from_pandas_edgelist(df, source='from', target='to')
    if(axes==None):
        nx.draw(G, with_labels=False, node_size=50, node_color="skyblue", ax=axes, pos=nx.fruchterman_reingold_layout(G))
    else:
        nx.draw(G, with_labels=False, node_size=50, node_color="skyblue", ax=axes, pos=nx.fruchterman_reingold_layout(G))
    plt.title("fruchterman_reingold")
    plt.savefig(name)
    if(close):
        plt.close()
        
def draw2(matrix, name, close, axes):
    A, B = np.where(matrix == 1)
    A = list(A)
    B = list(B)
    df = pd.DataFrame({'from': A, 'to': B})
    G = nx.from_pandas_edgelist(df, source='from', target='to')
    if(axes==None):
        nx.draw(G, with_labels=False, node_size=50, node_color="skyblue", ax=axes, pos=nx.kamada_kawai_layout(G))
    else:
        nx.draw(G, with_labels=False, node_size=50, node_color="skyblue", ax=axes, pos=nx.kamada_kawai_layout(G))
    plt.title("Kamada-Kawai")
    plt.savefig(name)
    if(close):
        plt.close()
