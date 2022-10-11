from .measurement_series_1 import *
from .measurement_series_2 import *
from .measurement_series_3 import *
from .measurement_series_4 import *

import numpy as np

all_fruits = np.concatenate((all_fruits_m1_cleaned, all_fruits_m2,
                             day_m3_all_fruit_interpolated))

all_fruits_new = np.concatenate((all_fruits_m1_cleaned, all_fruits_m2,
                             day_m3_all_fruit_interpolated, all_fruits_m4))
