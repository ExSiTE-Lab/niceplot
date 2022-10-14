import matplotlib,os
import matplotlib.pyplot as plt #https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.html
import matplotlib.tri as tri
import numpy as np

defaultcmap=matplotlib.cm.inferno
params={'font':{'family':'arial', 'weight':'regular' , 'size':16},
	'axes':{'titlesize':16},
	'figure':{'figsize':(8,6),'dpi':192}}
for key in params:
	matplotlib.rc(key, **params[key])

def contour(zvals,xvals,yvals,filename='',heatOrContour="heat",**kwargs):
	plt.clf() # need this or you get duplicate cbars if you generate multiple plots! 

	LB,UB=np.amin(zvals),np.amax(zvals)
	if "zlim" in kwargs.keys():
		zlim=kwargs["zlim"] ; LB={True:LB,False:zlim[0]}[zlim[0] is None] ; UB={True:UB,False:zlim[1]}[zlim[1] is None]

	# for heatmaps, you can use tricontourf, but that won't work for contours. need to follow https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html
	if len(np.shape(zvals))!=2:
		# Create grid values first.
		xi = np.linspace(min(xvals), max(xvals), 1000)
		yi = np.linspace(min(yvals), max(yvals), 1000)
		# Linearly interpolate the data (x, y) on a grid defined by (xi, yi).
		triang = tri.Triangulation(xvals, yvals)
		interpolator = tri.LinearTriInterpolator(triang, zvals)
		Xi, Yi = np.meshgrid(xi, yi)
		zi = interpolator(Xi, Yi)
		xvals=Xi ; yvals=Yi ; zvals=zi

	if heatOrContour in ["heat","both"]:
		CS=plt.contourf(xvals,yvals,zvals,levels=np.linspace(LB,UB,500),cmap=kwargs.get("cmap",defaultcmap))
		cbar=plt.colorbar()
		for c in CS.collections:
			c.set_edgecolor("face")
		#	c.set_rasterized(True)
		#nDecimals=int(scientificNotation(UB-LB).split("e")[1])*-1+1
		#nDecimals=max(nDecimals,0) # https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros
		#cbar.ax.set_yticklabels([format(v,'.'+str(nDecimals)+'f') for v in cbar.get_ticks()])
	if heatOrContour in ["contour","both"]:
		levels=np.linspace(LB,UB,20)
		contourKwargs={"levels":levels,"linestyles":kwargs.get("linestyle","-"),"linewidths":kwargs.get("linewidth",1)}
		color=kwargs.get("linecolor","black") ; colorOrMap={True:"cmap",False:"colors"}[ color in matplotlib.colormaps.keys() ]
		contourKwargs[colorOrMap]=color
		CS=plt.contour(xvals,yvals,zvals, **contourKwargs)
		#if linelabels:
		#	pltObj.clabel(CS, inline=1)
	# GENERAL
	plt.title( kwargs.get("title","TITLE") )
	plt.xlabel(kwargs.get("xlabel","XLABEL") )
	plt.ylabel(kwargs.get("ylabel","YLABEL") )
	
	if "overplot" in kwargs.keys(): # it's possible to pass a dict of xs,ys,markers, to be plotted over top of the contour/heatmap
		for dataset in kwargs["overplot"]:
			xs=dataset["xs"] ; ys=dataset["ys"] ; kind=dataset["kind"] # these are the only 3 required keys! all else is kwargs
			kw={ k:dataset[k] for k in dataset.keys() if k not in ["xs","ys","kind"] }
			if kind=="scatter":
				plt.scatter(xs,ys,**kw)	
			elif kind=="line":
				plt.plot(xs,ys,**kw)
			elif kind=="text":		# TODO consider using annotate instead? https://stackoverflow.com/questions/14432557/scatter-plot-with-different-text-at-each-data-point this buys you arrows, and you can still do plt.annotate
				text=kw["text"]		# text-type overplotting has one more required key: "text"
				kw={ k:kw[k] for k in kw.keys() if k!="text" }
				for x,y,t in zip(xs,ys,text):
					plt.text(x,y,t,**kw)

	if len(filename)>0:
		if ".svg" in filename:
			matplotlib.rc("svg", **{'fonttype':'none'}) # ensures text in svg files is saved as text (for later editing)
		plt.savefig(filename)
	else:
		plt.show()