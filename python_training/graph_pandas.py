import pandas as pd
import matplotlib.pyplot as plt

y = [700,1000,600,800,600,750,800]
x = [1,2,3,4,5,6,7]
graph = pd.DataFrame (y,x)
graph.plot (kind='line')
plt.show()