import matplotlib,os
import matplotlib.pyplot as plt #https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.html
import numpy as np

cmap=matplotlib.cm.inferno
params={'font':{'family':'arial', 'weight':'regular' , 'size':16},
	'axes':{'titlesize':16},
	'figure':{'figsize':(8,6),'dpi':192}}
for key in params:
	matplotlib.rc(key, **params[key])

def contour(zvals,xvals,yvals,filename='',heatOrContour="heat",**kwargs):
	LB,UB=np.amin(zvals),np.amax(zvals)
	if heatOrContour in ["heat","both"]:
		plt.contourf(xvals,yvals,zvals,levels=np.linspace(LB,UB,500),cmap=cmap)
		cbar=plt.colorbar()
		#nDecimals=int(scientificNotation(UB-LB).split("e")[1])*-1+1
		#nDecimals=max(nDecimals,0) # https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros
		#cbar.ax.set_yticklabels([format(v,'.'+str(nDecimals)+'f') for v in cbar.get_ticks()])
	if heatOrContour in ["contour","both"]:
		levels=np.linspace(LB,UB,20)
		CS=plt.contour(xvals,yvals,zvals,colors="black",levels=levels,linestyles="-")
		#if linelabels:
		#	pltObj.clabel(CS, inline=1)
	# GENERAL
	plt.title( kwargs.get("title","TITLE") )
	plt.xlabel(kwargs.get("xlabel","XLABEL") )
	plt.ylabel(kwargs.get("ylabel","YLABEL") )

	if len(filename)>0:
		if ".svg" in filename:
			matplotlib.rc("svg", **{'fonttype':'none'}) # ensures text in svg files is saved as text (for later editing)
		plt.savefig(filename)
	else:
		plt.show()