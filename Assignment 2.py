# Importing libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Read the dataset
fts = pd.read_csv('D:\\Sabiha\\pythonProject2\\data.csv')
fts.head()

#Check out the number of columns
fts.shape

#List all column names
print(fts.columns)

#Calculating correlation between each pair of variables

corr_matrix = fts.corr()


#Creating a seaborn heatmap
plt.figure(1, figsize=(10, 8))
sns.heatmap(corr_matrix, cmap='BrBG', center=0, annot=True, square=True)
plt.title('Correlation Heatmap')
plt.show()

#Features ‘city mpg’ and ‘highway MPG’ have a strong positive correlation with a value of 0.89
#Features ‘Engine Cylinders’ and ‘Engine HP’ also have a strong positive correlation with a value of 0.78

