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

final_areas = np.zeros(50)
x_coord = 0
y_coord = 0

for coord in range(dists.shape[0]):
  coord_sort = np.sort(dists[coord])
  coord_sort_args = np.argsort(dists[coord])
  if (coord_sort[0] != coord_sort[1]):
    if final_areas[coord_sort_args[0]] == -1:
      if (y_coord == ymax+1):
        y_coord = 0
        x_coord = x_coord + 1
      else:
        y_coord = y_coord + 1
      continue
    elif (x_coord == xmin or x_coord == xmax+1 or y_coord == ymin or y_coord == ymax+1):
      final_areas[coord_sort_args[0]] = -1
    else:
      final_areas[coord_sort_args[0]] = final_areas[coord_sort_args[0]] + 1
  
  if (y_coord == ymax+1):
    y_coord = 0
    x_coord = x_coord + 1
  else:
    y_coord = y_coord + 1

print(max(final_areas))