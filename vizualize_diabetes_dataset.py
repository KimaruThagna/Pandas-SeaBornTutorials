# Univariate Histograms
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
import numpy as np
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(url, names=names)# a way of obtaining datasets without downloading CSVs
data.hist()
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
#boxplots and density plots are used to study the distribution of attributes
#with box plots, the box is drawn around the 25th and 75th percentile and the whiskers
#give an idea of the spread of data dots outside the whiskers show potential outliers
correlations = data.corr()
# plot correlation matrix
# correlation matrix gives an indication of how related the changes are between 2 variables
#this is important since variables can be positively or negatively correlated and thus affect
#algorithm performance eg, logistic and linera regression can have poor performance with
#highly correlated data
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
scatter_matrix(data)
plt.show()