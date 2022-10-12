import numpy as np
from nicecontour import *

xs=np.linspace(-10,10,100)
ys=np.linspace(-10,10,100)
zs=xs[:,None]**2-10*np.sin(ys[None,:])

#contour(zs,xs,ys,heatOrContour="both")
#contour(zs,xs,ys,heatOrContour="both",cmap="viridis")
#contour(zs,xs,ys,heatOrContour="both",linestyle=":")
ls=[":"]*30 ; ls[5]="-"
#contour(zs,xs,ys,heatOrContour="both",linestyle=ls,linewidth=3)
contour(zs,xs,ys,heatOrContour="both",linestyle=ls,linecolor=["black"]*5+["red"]+["black"]*40)