# niceplot
A simple matplotlib wrapper which enables single-call plot generation, without needing to include all the matplotlib setup calls every time. Several "rules" for generating visually-appealing scientific plots are also included (e.g. requiring axis labels).

Basic useage: 
```
# import
from niceplot import *

# generate your data
xs=np.linspace(0,10,20)
ys=xs**2

# plot the data. first two arguments are list of x,y datasets.
# markers argument includes a list of markers for datasets (sensible defaults will be attempted), labels go in the legend. 
# and additional keyword args are accepted, e.g. "title" which is passed through to matplotlib's ax.set_title and so on
plot([xs,xs],[ys,ys/2],markers=['k.','#882e2e,^'],title="black line, reddish triangles",labels=["x^2","1/2*x^2"])
```
