"""
Jason de Mey, V2B

This project is a run through the starter tutorial of Mesa.
https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html
"""

from money_model import *
import matplotlib.pyplot as plt
import numpy as np

model = MoneyModel(50, 10, 10)
for i in range(100):
    model.step()

# To visualize the number of agents residing in each cell:
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()

# To get the series of Gini coefficients as a pandas DataFrame:
gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.show()

# agent_wealth = model.datacollector.get_agent_vars_dataframe()
# agent_wealth.head()