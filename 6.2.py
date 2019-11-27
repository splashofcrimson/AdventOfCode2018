import numpy as np
import itertools
from scipy import spatial

coordinates = np.zeros((50, 2))
for i in range(0, 50):
  coordinate = input()
  coordinate_split = coordinate.split(',')
  coordinates[i, 0] = int(coordinate_split[0])
  coordinates[i, 1] = int(coordinate_split[1])

xmin = 0
xmax = int(np.max(coordinates[:,0]))
ymin = 0
ymax = int(np.max(coordinates[:,1]))

plane_rows = np.arange(int(xmax)+2)
plane_cols = np.arange(int(ymax) + 2)
plane = np.array(list(itertools.product(plane_rows, plane_cols)))
dists = spatial.distance.cdist(plane, coordinates, 'cityblock')

dist_sums = np.sum(dists, axis=1)
print(dist_sums[dist_sums < 10000].shape[0])
