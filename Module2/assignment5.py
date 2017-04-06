import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#
df = pd.read_csv('Datasets/census.data', header = None, index_col = 0)

headers = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex','classification']
df.columns = headers
# df_column_fix = df.drop('number', axis = 1)

#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# df_column_fix.dtypes
df = df.replace('?', np.NaN)
# df_type_fix = df_nan_fix['capital-gain']

# s = pd.Series([df_nan_fix['capital-gain']])

# pd.to_numeric(s)

df['capital-gain'] = pd.to_numeric(df['capital-gain'])

#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#

df['education'].astype('category')
df['classification'].astype('category')

pd.get_dummies(df['race'])
pd.get_dummies(df['sex'])

#
# TODO:
# Print out your dataframe
#
# .. your code here ..


