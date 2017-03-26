import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
df = pd.read_csv('Datasets/tutorial.csv')


# TODO: Print the results of the .describe() method
#
first_look = df.describe()
print(first_look)

# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
new_df = df.loc[2:4, 'col3']
print(new_df)

results = new_df.describe()
print(results)