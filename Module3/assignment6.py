import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds_dataset = pd.read_csv('Datasets/wheat.data', index_col = 0)

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
# .. your code here ..


#
# TODO: Compute the correlation matrix of your dataframe
# 
corr_matrix = seeds_dataset.corr('pearson')

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
plt.imshow(corr_matrix, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(seeds_dataset.columns))]
plt.xticks(tick_marks, seeds_dataset.columns, rotation='vertical')
plt.yticks(tick_marks, seeds_dataset.columns)

plt.show()


#
# This code is intentionally missing!
# Read the directions on the course lab page!
#

