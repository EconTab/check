import numpy as np

demo_array = np.arange(10,21)
subset_demo_array = demo_array[0:7]
subset_demo_array[:] = 101
subset_demo_array