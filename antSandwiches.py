import pandas as pd
# import numpy as np
# pandas dataframe - similar to an excel table

# 3 ways of creating a dataframe - One method is manually creating
# https://www.geeksforgeeks.org/python-pandas-dataframe-values/
# Second method is importing a file and converting to DF
dataset = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Stat2Data/SandwichAnts.csv')

bread_set = set()
filling_set = set()
sandwich_dict = {}
filling_dict = {}

for row in dataset.values:
    if row[2] not in bread_set:
        bread_set.add(row[2])
        sandwich_dict[row[2]] = [row[5]]
    else:
        sandwich_dict[row[2]].append(row[5])

    if row[3] not in filling_set:
        filling_set.add(row[3])
        filling_dict[row[3]] = [row[5]]
    else:
        filling_dict[row[3]].append(row[5])

### First glance @ the dataset ###
rows, cols = dataset.shape # df.shape
# print(f'In the dataset there are {rows} rows and {cols} columns')
# print(dataset.info()) # Show Datatypes
# print(dataset.describe()) # Show All Stats (count, mean, std, mean, max)
# print(dataset) # Show whole dataset
# print(dataset.tail()) # Show last few rows

avg_ants = dataset['Ants'].mean()
print(f"On average, there are {avg_ants} ants on any given sandwich")

bread_data = pd.DataFrame(sandwich_dict) # Convert dictionary to DataFrame
filling_data = pd.DataFrame(filling_dict)
# print(bread_set)
# print(filling_set)
# print(bread_data)
# print(filling_data)

above_avg = {}
below_avg = {}
for key in filling_set:
    num_ants = filling_data[key].mean() 
    if num_ants < avg_ants:
        below_avg[key] = num_ants 
    else:
        above_avg[key] = num_ants

for key in bread_set:
    num_ants = bread_data[key].mean() 
    if num_ants < avg_ants:
        below_avg[key] = num_ants 
    else:
        above_avg[key] = num_ants


print(f'Below avg: {below_avg}')
print(f'Above avg: {above_avg}')

# Export dataframe to file
# results.to_filetype('results.csv')

bread_correlations = {
    'White': bread_data['White'].corr(dataset['Ants']),
    'WholeWheat': bread_data['WholeWheat'].corr(dataset['Ants']),
    'MultiGrain': bread_data['MultiGrain'].corr(dataset['Ants']),
    'Rye': bread_data['Rye'].corr(dataset['Ants'])
}
print(bread_correlations)

filling_correlations = {
    'Vegemite': filling_data['Vegemite'].corr(dataset['Ants']),
    'PeanutButter': filling_data['PeanutButter'].corr(dataset['Ants']),
    'HamPickles': filling_data['HamPickles'].corr(dataset['Ants']),
}
print(filling_correlations)

# print(dataset[dataset.columns[2:]])
# print(pd.concat([bread_data, filling_data], axis=1, keys=["bread_data", "filling_data"]).corr())
# print(corr.columns[:][0])
# Crazy correlation between two dataframes
# https://stackoverflow.com/questions/41823728/how-to-perform-correlation-between-two-dataframes-with-different-column-names
corr = pd.concat([bread_data, filling_data], axis=1, keys=["bread_data", "filling_data"]).corr().loc['bread_data', 'filling_data']
print(corr)
# print(dataset)