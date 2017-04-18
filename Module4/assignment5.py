import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
import os

samples = []
samples_i = []
colors = []
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
files = os.listdir('Datasets/ALOI/32')

for file_name in files:
  img = misc.imread( os.path.join('Datasets/ALOI/32', file_name) )
  file_name.colors = 'b'
  samples.append(  (img[::2, ::2] / 255.0).reshape(-1)  )
    
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#


#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
files_i = os.listdir('Datasets/ALOI/32i')

for file_name in files_i:
  img = misc.imread( os.path.join('Datasets/ALOI/32i', file_name) )
  samples_i.append(  (img[::2, ::2] / 255.0).reshape(-1)  )
  samples.extend(samples_i)
#
# TODO: Convert the list to a dataframe
#
samples = pd.DataFrame( samples )
#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
from sklearn import manifold

iso = manifold.Isomap(n_neighbors = 6, n_components = 3)
iso.fit(samples)
manifold = iso.transform(samples)
manifold = pd.DataFrame( manifold )


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#

manifold.plot.scatter( 0, 1, c = colors )

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

