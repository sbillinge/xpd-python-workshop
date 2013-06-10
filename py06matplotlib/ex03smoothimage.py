#!/usr/bin/env python

"""\
INSTRUCTIONS:

(1) Read in the "dc_metro.png" image and plot it using the "gray" colormap.

(2) Use an averaging filter to "smooth" the image.  Use a "5 point stencil"
    where you average the current pixel with its neighboring pixels:

              0 0 0 0 0 0 0
              0 0 0 x 0 0 0
              0 0 x x x 0 0
              0 0 0 x 0 0 0
              0 0 0 0 0 0 0

Plot the image, the smoothed image, and the difference between the two.

HINT: Check documentation for matplotlib functions "imread" and "imshow".
"""

import numpy as np
import matplotlib.pyplot as plt

# +++your code here+++

plt.show()
