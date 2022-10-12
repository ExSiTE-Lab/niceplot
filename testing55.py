import numpy as np
from nicecontour import *

xs=np.linspace(-10,10,1000)
ys=np.linspace(-10,10,1000)
zs=xs[:,None]**2-10*np.sin(ys[None,:])

contour(zs,xs,ys,heatOrContour="both")