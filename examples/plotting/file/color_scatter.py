from __future__ import unicode_literals
from future.builtins import zip

import numpy as np

from bokeh.plotting import *

N = 4000

x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]

output_file("color_scatter.html", title="color_scatter.py example")

scatter(x,y, radius=radii, radius_units="data",
       fill_color=colors, fill_alpha=0.6,
       line_color=None, tools="pan,zoom,save,resize", name="color_scatter_example")

if __name__ == "__main__":
    show()  # open a browser
