#import pip
#pip.main(["install","matplotlib"])
import numpy as np
import matplotlib.pyplot as plt

ys = 500 + np.random.randn(499)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 497, where=(ys > 497), facecolor='r', alpha=0.5)

plt.title("Sample Plot from Matplotlib")
plt.show()
