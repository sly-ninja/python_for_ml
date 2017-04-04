import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds_dataset = pd.read_csv('Datasets/wheat.data', index_col = 0)


#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
truncated_dataset = seeds_dataset.drop(['area', 'perimeter'], axis = 1)


#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
parallel_coordinates(truncated_dataset, 'wheat_type', alpha = 0.4)


plt.show()

#http://stackoverflow.com/questions/8230638/parallel-coordinates-plot-in-matplotlib


