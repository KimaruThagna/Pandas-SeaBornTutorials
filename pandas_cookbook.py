import pandas as pd
import numpy as np
df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5],[3, 4, np.nan, 1], [3, 4, 0, 1]], columns=list('ABCD'))
#df.shape()
df.drop_duplicates()
df.dropna(axis=1, how='all') #remve all column where all value is 'NaN' exists
df.dropna(axis=0, how='all') #remve all row where all value is 'NaN' exists
# how=any
df.dropna(thresh=2) #remve all row if there is non-'NaN' value is less than 2
df.dropna(axis=0, subset=['A']) #remove row where if there is any 'NaN' value in column 'A'
df.dropna(axis=1, subset=[1]) #remove column  if there is any 'NaN' value in index is '1'
df.info()

wine=pd.read_csv('winequality-red.csv',header=0,delimiter=';')
print(wine.head())

chlorides=wine.loc[:,'chlorides'] # all rows in the one column
sulphurs=wine.loc[:,['free sulfur dioxide','total sulfur dioxide']] # all rows in the specified cols
acid_data=wine.loc[:,'fixed acidity':'residual sugar'] # all rows from colx to coly
print(wine.describe() )
max_val = wine.max(numeric_only=True) #collects only numeric columns
#wine.describe(include=['0']) #this includes also description of non numeric data
# assume a dataset called financials
# cities_usa = financials.hq_location[financials["country"] == "USA"].value_counts().head()
# sector_china = financials.sector[financials["country"] == "China"].value_counts().head(3)
# neutral_ph = financials.pH[wine["pH"] == 7].mean()
#convert column to datetime
#financials['DATE'] = pd.to_datetime(financials['DATE'])

# data vizualization tips and tricks


# plt.legend(loc='upper right') location of legend
# ax.tick_params(bottom="off", top="off", left="off", right="off") removing ticks
# removing spines for all axes
# ax.spines["right"].set_visible(False)
# for key, spine in ax.spines.items():
# spine.set_visible(False)
# https://www.gooddata.com/blog/5-data-visualization-best-practices
#
# in data vizualization, enusre the data-ink ratio is maintained such that data is more profound
# in case of multiple plots, label the right and left most plots
# remove spines,axes and grid lines