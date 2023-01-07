import matplotlib,os
import matplotlib.pyplot as plt #https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.html
import matplotlib.tri as tri
import numpy as np
from niceplot import processText

defaultcmap=matplotlib.cm.inferno
params={'font':{'family':'arial', 'weight':'regular' , 'size':16},
	'axes':{'titlesize':16},
	'axes':{'autolimit_mode':'round_numbers'},
	'figure':{'figsize':(8,6),'dpi':192}}

def setContRC(key,para):
	matplotlib.rc(key, **para)
for key in params:
	setContRC(key,params[key]) # replaces "matplotlib.rc(key, **params[key])"

def contour(zvals,xvals,yvals,filename='',heatOrContour="heat",useLast=False,**kwargs):
	global fig,ax,CS
	if not useLast:
		fig,ax=plt.subplots()
		plt.clf() # need this or you get duplicate cbars if you generate multiple plots! 

	# if we're saving files, use the "Agg" backend. (and save off whatever the current backend is, and restore it after we save it, to prevent messing up the user's python environment). if we're showing, just default to whatever the user's default is
	backend=matplotlib.get_backend()
	if len(filename)!=0:# and filename!="PLOTOBJ":
		matplotlib.use("Agg") # https://stackoverflow.com/questions/31156578/matplotlib-doesnt-release-memory-after-savefig-and-close

	#if len(filename)==0:
	#	# if macos error, try: "export MPLBACKEND=TKAgg" https://stackoverflow.com/questions/55811545/importerror-cannot-load-backend-tkagg-which-requires-the-tk-interactive-fra
	#	matplotlib.use("TkAgg") # https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so
	#else:
	#	matplotlib.use("Agg") # https://stackoverflow.com/questions/31156578/matplotlib-doesnt-release-memory-after-savefig-and-close

	LB,UB=np.nanmin(zvals),np.nanmax(zvals)
	if "zlim" in kwargs.keys():
		zlim=kwargs["zlim"] ; LB={True:LB,False:zlim[0]}[zlim[0] is None] ; UB={True:UB,False:zlim[1]}[zlim[1] is None]
	nticks=kwargs.get("nticks",10)
	print(LB,UB)
	ticks=kwargs.get("zticks",np.linspace(LB,UB,nticks))
	
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
		#print(np.amin(zvals),np.amax(zvals))
		cbar=plt.colorbar(ticks=ticks)
		for c in CS.collections:
			c.set_edgecolor("face")
		#	c.set_rasterized(True)
		nDecimals=max(0,int(1-np.floor(np.log(UB-LB)/np.log(10)))) # 0.35-0 --> -0.4559319556497244 --> -1 --> could be represented at 3.5e-1. if it was 35, we'd want 0 decimals. if it was 3.5 we'd want 1 decimal. -1 we want 2. 350, we still want 0 decimals
		#print(nDecimals)
		#nDecimals=max(nDecimals,0) # https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros
		ticks=cbar.get_ticks()
		ticks=[ format(v,'.'+str(nDecimals)+'f') for v in ticks]
		cbar.ax.set_yticklabels(ticks)
		cbar.ax.set_title(kwargs.get("zlabel","ZTITLE"))
	# TODO should contours have cbars? no need, if inline labels are used...
	# TODO beware: useLast=True -> no plt.clf() -> if heatmap is used, duplicative cbars will result. this might be okay though? because overlapping a heatmap seems like nonsense?
	if heatOrContour in ["contour","both"]:
		levels=kwargs.get("levels",np.linspace(LB,UB,20))
		contourKwargs={"levels":levels,"linestyles":kwargs.get("linestyle","-"),"linewidths":kwargs.get("linewidth",1)}
		color=kwargs.get("linecolor","black") ; colorOrMap={True:"cmap",False:"colors"}[ color in matplotlib.colormaps.keys() ]
		contourKwargs[colorOrMap]=color
		CS=plt.contour(xvals,yvals,zvals, **contourKwargs)
		#if heatOrContour!="both":
		#	cbar=plt.colorbar()
		if kwargs.get("inline",False):
			plt.clabel(CS, inline=1)
	# GENERAL
	plt.title( processText( kwargs.get("title","TITLE") ) )
	plt.xlabel( processText( kwargs.get("xlabel","XLABEL") ) )
	plt.ylabel( processText( kwargs.get("ylabel","YLABEL") ) )
	plt.xlim( kwargs.get("xlim",None) )
	plt.ylim( kwargs.get("ylim",None) )
	#plt.clim( kwargs.get("zlim",None) )
	
	if "overplot" in kwargs.keys(): # it's possible to pass a list of dicts of xs,ys,markers, to be plotted over top of the contour/heatmap
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

	matplotlib.use(backend)
	#return CS

def getContObjs():
	return ax,fig
def getCS():
	return CS