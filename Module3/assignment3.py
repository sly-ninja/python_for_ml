import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds_dataset = pd.read_csv('Datasets/wheat.data', index_col = 0)


fig = plt.figure()

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
s1 = fig.add_subplot(111, projection = '3d')
s1.set_xlabel('area')
s1.set_ylabel('perimeter')
s1.set_zlabel('asymmetry')

s1.scatter(seeds_dataset['area'], seeds_dataset['perimeter'], seeds_dataset['asymmetry'], c = 'r', marker = '.')
plt.show()


#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
fig = plt.figure()

s2 = fig.add_subplot(111, projection = '3d')
s2.set_xlabel('width')
s2.set_ylabel('groove')
s2.set_zlabel('length')

s2.scatter(seeds_dataset['width'], seeds_dataset['groove'], seeds_dataset['length'], c = 'g', marker = '.')

plt.show()


