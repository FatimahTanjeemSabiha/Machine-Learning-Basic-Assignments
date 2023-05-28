# Importing libraries
import pandas as pd

# Read csv file into a pandas dataframe
ss = pd.read_csv('D:\\Sabiha\\Lab Task-1\\brfss.csv')

# Create a function cleanBRFSSFrame() to clean the dataset
def cleanBRFSSFrame(ss):
    # Drop the sex from the dataframe
    ss = ss.drop("sex", axis=1)

    # Drop the rows of NaN values
    ss = ss.dropna()
    return ss
cleaned_ss = cleanBRFSSFrame(ss)

print(cleaned_ss)

# Use the describe() method to display the count, mean, std, min, and quantile data for column weight2
print(ss["weight2"].describe())

# Find the median of the age
print(ss["age"].median())

# Find the mode of the age
print(ss["age"].mode())