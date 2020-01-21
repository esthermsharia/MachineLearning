import seaborn as sns
import pandas as pd
#Seaborn is part of the pydata stack hence it will accept pandas data structures
#Importing the dataset using pandas.
housing_url="/home/david/Desktop/fCharlie/gapminder-FiveYearData.csv"
df=pd.read_csv(housing_url)
#Creating the pivot table with country along the y-axis and year along the x-axis.
pivot_table=df.pivot('country','year','lifeExp')
#plotting the heatmap.
sns_plot=sns.heatmap(pivot_table)

#Saving the plot
sns_plot.figure.savefig("output.png")