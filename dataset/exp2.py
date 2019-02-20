import numpy as np

from matplotlib import pyplot as plt

from sompy import SOM 


input_data = np.random.rand(1000, 3)


output_shape = (40, 40)


som = SOM(output_shape, input_data)


som.set_parameter(neighbor=0.26, learning_rate=0.22)
 

output_map = som.train(10000)

plt.imshow(output_map, interpolation='none')
plt.show()
