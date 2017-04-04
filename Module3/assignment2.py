import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds_dataset = pd.read_csv('Datasets/wheat.data')

#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
seeds_dataset.plot.scatter(x = 'area', y = 'perimeter')

#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
seeds_dataset.plot.scatter(x = 'groove', y = 'asymmetry')

#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
seeds_dataset.plot.scatter(x = 'compactness', y = 'width')


# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


