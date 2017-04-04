#
# This code is intentionally missing!
# Read the directions on the course lab page!
#

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

plt.style.use('ggplot')

seeds_dataset = pd.read_csv('Datasets/wheat.data', index_col = 0)
truncated_dataset = seeds_dataset.drop(['area', 'perimeter'], axis = 1)

andrews_curves(truncated_dataset, 'wheat_type', alpha = 0.4)
andrews_curves(seeds_dataset, 'wheat_type', alpha = 0.4)

plt.show()
