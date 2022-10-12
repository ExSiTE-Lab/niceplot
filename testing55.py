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
#contour(zs,xs,ys,heatOrContour="both",linestyle=ls,linecolor=["black"]*5+["red"]+["black"]*40)
#contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis")
mkr="." ; c=np.linspace(0,1,100)
#contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis",overplot=[{"xs":xs,"ys":xs**3/100,"kind":"scatter","marker":mkr,"c":c},{"xs":xs,"ys":xs**2/10,"kind":"line","linestyle":"-","color":"black"}])
scatx=xs[::5] ; scaty=scatx**3/100
texts=[ str(np.round(x,1))+","+str(np.round(y,1)) for x,y in zip(scatx,scaty) ]
contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis", overplot=[{"xs":scatx,"ys":scaty,"kind":"scatter","marker":mkr,"c":"red"},{"xs":scatx+2,"ys":scaty+2,"kind":"text","text":texts,"fontsize":20}])
