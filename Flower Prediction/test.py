import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

x_npz = np.load("flowers.npz")

x = x_npz['arr_0']

plt.imshow(x[1])
plt.show()
print("hello")
