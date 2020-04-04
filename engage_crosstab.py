import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 

def main ():
	#read in files auditors.csv, prices.csv, stores.json
	auditorsDF = pd.read_csv('auditors.csv')
	pricesDF = pd.read_csv('prices.csv')
	storesDF = pd.read_json('stores.json')

	#as long as data is present in prices and stores merge frames
	if (pricesDF is not None and auditorsDF is not None):
		df = pricesDF

		if (storesDF is not None):
			df2 = pd.merge(df, storesDF, on="Store ID", how='outer')

	#crosstab https://pbpython.com/pandas-crosstab.html
	if (df2 is not None):
		output = pd.crosstab(
				index=[df2.Banner, df2.UPC],
				columns=df2.Region,
				margins=True,
				values=df2.Price,
				dropna=False,
				aggfunc='mean'
				).round(2)

	#heatmap visualization of data
	fig=plt.figure(figsize=(12,8))
	ax=fig.add_subplot(111)
	sns.heatmap(output,
            cmap="YlGnBu", annot=False, cbar=False)
	ax.set_title("Heatmap Regional Prices Visualization")
	plt.tight_layout()
	plt.show()

	if (output is not None):
		output.to_csv("engage_solution.csv", index=True)

if __name__ == '__main__':
	main()
