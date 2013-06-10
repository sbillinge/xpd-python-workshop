#!/usr/bin/env python

"""\
INSTRUCTIONS:

(1) Plot ellipse with the main axes a=2, b=1.  Make sure the ellipse is
    drawn at correct aspect ratio.

(2) Export the figure in EPS format to an ex02ellipse.eps file.

HINT: Check documentation for matplotlib functions "axis" and "savefig".
"""

import numpy as np
import matplotlib.pyplot as plt

# clear the current figure
plt.clf()

phi = np.linspace(0, 2 * np.pi, 400)
# +++your code here+++

# redraw and display the figure window
plt.draw()
plt.show()
