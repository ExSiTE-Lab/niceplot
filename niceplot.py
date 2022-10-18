import matplotlib,os
import matplotlib.pyplot as plt #https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.html
import numpy as np
from cycler import cycler

# THESE ARE ALL YOUR USER-CONFIGURABLE SETTINGS.
# WHAT DEFAULT COLORS AND SYMBOLS DO YOU WANT TO ROTATE THROUGH? WHAT COLORMAP DO YOU WANT INTEGER COLOR VALUES TO REFER TO?
defCols=['k', 'g', 'b', 'r']
defMark=['o','^','s','P','d','X','v','+','x']
defaultMarkerSize = 10
defaultLineWidth = 2
cycle=cycler(color=defCols*len(defMark))+cycler(marker=defMark*len(defCols)) # https://github.com/matplotlib/cycler/issues/41
#cmap=matplotlib.cm.inferno
#cmap=matplotlib.cm.rainbow
cmap=matplotlib.cm.plasma
# WHAT GLOBAL TICK, AXIS, FONT SETTINGS DO YOU WANT?
params={ 'xtick':{'direction':'in', 'top':True , 'bottom':True , 'major.pad':7 }, # (rule #4)
	'ytick':{'direction':'in', 'left':True , 'right':True , 'major.pad':7 },
	'font':{'family':'arial', 'weight':'regular' , 'size':16}, # (rule #5)
	'axes':{'autolimit_mode':'round_numbers',"prop_cycle":cycle, 'titlesize':16}, # (rule #6 Titile size should be the same size as the fontsize)
	#'svg':{'fonttype':'none'}, # ensure fonts in exported svgs are text objects wen you open them with inkscape: https://stackoverflow.com/questions/34387893/output-matplotlib-figure-to-svg-with-text-as-text-not-curves
	'figure':{'figsize':(8,6),'dpi':192},
	'legend':{'edgecolor':'black','fancybox':False}			# fancybox=false removes corner curvature
	
	}
for key in params:
	matplotlib.rc(key, **params[key])

markerSize = defaultMarkerSize ; lineWidth = defaultLineWidth

# RULES FOR PLOTTING:
# 1. plots must be generated in origin or matlab
# 2. Axes must be labeled with both title and unit
# 3. Border must appear on all edges of plot area
# 4. ticks must be set to "in"
# 5. the same font style (Arial) and sizes must be used for plot labels, units, tick number labels
# 6. the values of the ticks at the beginning and end of axes must be clearly labeled. "reasonable and legible" tick number labels must be chosen for ticks.
# 7. if linear scale, the axis values must start at (or span across) zero
# 8. all data and labels must be legible when printed in black and white. symbols should be clearly differentiable, legends should be clear and discernible from data being presented, data should be easily interpretable. 
# Answers: 2 is encouraged by giving the user dummy labels which should be in obvious need of attention. 3,4,5,6 are handled via rcparams (tick location, direction, font, autolimit_mode). 7 is handled via a manual set_xlim set_ylim right before incorporating kwargs. 8 is addressed in part by sensible default color/marker/linestyle choices. 

# ASK MATPLOTLIB WHAT MARKERS/LINESTYLES/COLOR SHORTCUTS ARE AVAILABLE
standardOptions={ "markers" : list(matplotlib.markers.MarkerStyle.markers.keys()) ,
		"linestyles" : list(matplotlib.lines.lineStyles.keys()) ,
		"colors" : list(matplotlib._color_data.BASE_COLORS.keys())+list(matplotlib._color_data.TABLEAU_COLORS.keys()) }

# plot() is a basic wrapper for the likes of: "plt.plot(...);plt.xlabel(...);...
#  ;plt.show() or plt.savefig() etc". It also takes advantage of as many 
#  rcparams as possible to adhere to the rules for plotting, and takes 
#  matplotlib rcparams as optional arguments to pass in.
# Arguments:
# xs - a 2D list of x values: list of datasets, each dataset it itself a list
# ys - a 2D list of y values
# ye - a list matching ys: error value(s) for each dataset may be list or float
# markers - a 1D list describing how each dataset should be plotted. 
#	piece 1 denotes color: may be a standard color code (https://matplotlib.
#	  org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html), or a 2 digit int 
#	  from 00-99 (see float2rgb(c) below).
#	piece 2 denotes form: may be a marker symbol (https://matplotlib.org/sta
#	  ble/api/markers_api.html), or a linestyle symbol https://matplotlib.or
#	  g/stable/gallery/lines_bars_and_markers/linestyles.html, OR, "fN" 
#	  where N denotes that we're to fill between this and another dataset. 
#	if 2-character colors or 2-character form is used, separate with comma
#	examples: "ko" is a black o. "b-" is a blue line. "00f0" denotes a red 
#	  band will be filled in between this dataset and another which also has
#	  "f0". tab:blue,o"
#	hidden feature for markers: you can also pass a list with dicts, and
#	  we'll just pass the dict into the plot functions (plot, errorbar,
#	  fill_between) as kwargs. you'll need to manually set things like 
#	  "color":"red", but you'll also be able to include bonus parameters
#	  like linewidth, markersize, alpha, etc.
# filename - if a filename is provided, we'll save the plot instead of showing
# multiplot - 3 methods: split (two plots side-by-side sharing a y axis), 
#  stacked (two plot one-above-another sharing x axis), shared (one plot with a
#  shared x axis and 2 y axes). pass a tuple: (method,[indicesList]) where 
#  indicesList is a list of which dataset (xs,ys) goes on which plot
# Notes on expectations: function can handle basic plotting of points (ax.plot,
#  marker args, etc), lines (linestyle args), errorbars (ax.errorbar, with both
#  marker or linestyle args), and fill_between (you can plot shaded error bands
#  by passing a pair of datasets, y+ye and y-ye, and filling between them). 
def plot( xs, ys, ye='', markers='', labels='', filename='', multiplot='', fontsize='', **kwargs):
	global axs,frames,fig,markerSize,lineWidth ; axs=[] ; frames=[]
	lineWidth = kwargs.get("lw", defaultLineWidth) ; markerSize = kwargs.get("ms", defaultMarkerSize);
	
	# CREATE THE PLOT OBJECTS
	if len(multiplot)>0:
		axs,fig=genMultiAx(**multiplot)
	else:
		fig,ax=plt.subplots() ; axs.append(ax)
		
	# PUT THE DATA ON THE PLOT
	for i in range(len(xs)):
		x=xs[i] ; y=ys[i] ; ax=axs[0]
		if len(axs)>1:
			ax=axs[multiplot["indices"][i]]
		# PROCESS MARKERS
		if len(markers)>i:
			kw=handleMarkers(markers[i]) # turns marker strings into a dict to pass to each plot function
		else:
			kw={"linestyle":'',"markersize":markerSize}
		# LABELS (for legend) ALSO GO IN KWARGS
		kw["label"]="dataset "+str(i+1)
		if len(labels)>i:
			kw["label"]=processText(labels[i])

		# ADD TO PLOT
		if len(ye)>i:							# ERRORBARS
			ax.errorbar(xs[i], ys[i], yerr=ye, capsize=2, **kw)
		elif "fill" in kw.keys():					# FILL BETWEEN
			for j in range(i,len(xs)):				# check all other datasets (all after this one!)
				if (i==j) or (j>=len(markers)):
					continue
				kw2=handleMarkers(markers[j])
				if "fill" in kw2.keys() and kw2["fill"]==kw["fill"]:
					del kw["fill"]				# we just used this to understand if handleMarkers wanted
					ax.fill_between(xs[i], ys[i], ys[j], **kw)	# us to do filling. so delete it
					break
		else:								# OR BASIC PLOT WITH POINTS OR LINES
			ax.plot(xs[i], ys[i], **kw)
	for ax in axs:
		if len(labels)==0 or max( [ len(lb) for lb in labels ] ) > 1:
			l=ax.legend()
			frames.append( l.get_frame() )
	#plt.legend()

	# HANDLE OTHER ARGUMENTS. Each allowable is mapped to a function, and a default
	if "xscale" not in kwargs.keys() or kwargs["xscale"]!="log":
		xlim=list(axs[0].get_xlim()) ; xlim.append(0) ; xlim=[min(xlim),max(xlim)] ; axs[0].set_xlim(xlim)
	if "yscale" not in kwargs.keys() or kwargs["yscale"]!="log":
		ylim=list(axs[0].get_ylim()) ; ylim.append(0) ; ylim=[min(ylim),max(ylim)] ; axs[0].set_ylim(ylim)

	axs[0].set_title( processText( kwargs.get("title","TITLE") ) ) # get "title" kw from kwargs, defaulting to "title". pass through
	axs[0].set_xlabel( processText( kwargs.get("xlabel","XLABEL") ) ) # processText, then set as title. and so on for xlabel,ylabel
	axs[0].set_ylabel( processText( kwargs.get("ylabel","YLABEL") ) ) 
	if "xlim" in kwargs.keys():
		axs[0].set_xlim( kwargs.get("xlim") )
	if "ylim" in kwargs.keys():
		axs[0].set_ylim( kwargs.get("ylim") )
	axs[0].set_xscale( kwargs.get("xscale","linear") )
	axs[0].set_yscale( kwargs.get("yscale","linear") )
	setFace( kwargs.get("facecolor","white") )
	if "figsize" in kwargs.keys():				# most are okay receiving None, except for set_size_inches
		fig.set_size_inches( kwargs.get("figsize") )
	if "fontsize" in kwargs.keys(): # https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
		#matplotlib.rc('font', **{'size': kwargs.get("fontsize") }) # TODO if you do this via rcparams, it "permanently" sets it for all following plots! not what we want
		#axs[0].set_font_size( kwargs.get("fontsize") )
		#axs[0].title.set_fontsize( kwargs.get("fontsize") )
		#matplotlib.rc('axes', **{'titlesize':kwargs.get("fontsize") })
		for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
			ax.get_xticklabels() + ax.get_yticklabels() + axs[0].get_legend().get_texts()):
			#item.set_fontsize(20)
			print(item)
			item.set_fontsize( kwargs.get("fontsize"))
		#for item in axs[0].get_legend().get_texts():
		#	print(item)
		#	item.set_fontsize( kwargs.get("fontsize"))

#'font':{'family':'arial', 'weight':'regular' , 'size':16}
	#		key	   set function   default val,  pre-function
#	funcLookup={ 	"title" : (axs[0].set_title , "TITLE" , processText) , 
#			"xlabel": (axs[0].set_xlabel, "XLABEL", processText) ,
#			"ylabel": (axs[0].set_ylabel, "YLABEL", processText) ,
#			"xlim"  : (axs[0].set_xlim  , None    , None       ) , 
#			"ylim"  : (axs[0].set_ylim  , None    , None       ) , 
#			"xscale": (axs[0].set_xscale, "linear", None       ) , 
#			"yscale": (axs[0].set_yscale, "linear", None       ) ,
#			"facecolor": (setFace       , "white" , None       ) ,
#			"figsize": (fig.set_size_inches, None , None       ) }
#	
#	for k in funcLookup.keys():		# for every allowed funct/arg
#		f,d,f2=funcLookup[k]
#		if k in kwargs.keys():		# if the user passed it, override the default with that
#			d=kwargs[k]		
#		if d is not None:		# if there's a value, set it
#			if f2 is not None:
#				d=f2(d)
#			f(d)			# replaces things like "ax.set_title(value)"

	if len(filename)>0:
		if ".svg" in filename:
			matplotlib.rc("svg", **{'fonttype':'none'}) # ensures text in svg files is saved as text (for later editing)
		plt.savefig(filename)
		plt.close() # without this, a later "show" will blast you by showing all previously-saved plots: https://mldoodles.com/matplotlib-save-plot-but-dont-show/
	else:
		plt.show()

# lots of valid options for markers: "k" (black, default in a symbol), "k-" (black line, mpl standard), "k,-" (comma-separated), "tab:blue" (blue, default in a symbol), "tab:blue,-" (blue line), "o" (default in the color, o symbol), "-" (defailt in the color, line symbol)
def handleMarkers(m):
	#print("m",m)
	kw={}
	#m=markers[i]
	if isinstance(m,str):
		if len(m)==0:
			return {"linestyle":'',"markersize":markerSize}
		if "," in m:						# COMMA-SEPARATED, color,form
			c,f=m.split(",")
		elif len(m)==2:						# OR DEFAULT TO char1,char2
			c,f=m[0],m[1:]					# TODO bug: "99" for purple --> "9","9". or "-." should be dash-dot
		else:							# length1, or n, try as both color and form
			c,f=m,m

		if "f" in f:						# FILL BETWEEN, e.g. "k,fABC" black, fill this and other "fABC"
			kw["fill"]=f#.replace("f","")			# (why not pass indices? this allows safe re-ordering of dsets)
			kw["linewidth"]=0
			kw["alpha"]=.2
		elif f in standardOptions["markers"]:			# MARKER, NOT LINESTYLE, e.g. "k.", dot
			kw["marker"]=f ; kw["linestyle"]=''; kw["markersize"]=markerSize
		elif f in standardOptions["linestyles"]:		# LINESTYLE, NOT MARKER, e.g. "b:", dotted line
			kw["marker"]='' ; kw["linestyle"]=f; kw["linewidth"]=lineWidth
		else:							# NEITHER, let mpl default in markers, suppress line
			kw["linestyle"]='' ; kw["markersize"]=markerSize

		if c in standardOptions["colors"] or c[0]=="#":			# STANDARD COLOR CODE
			kw["color"]=c
		else:
			for char in c:
				if char not in "0123456789":		# INVALID COLOR, we'll let mpl default in color
					break
			else:						# 2 DIGIT COLOR INSTEAD OF SHORTCUT CODE
				kw["color"]=float2rgb(int(c)/100)
		return kw
	return m

def genMultiAx(method,indices,scaling=''):
	axs=[] ; nPlots=len(set(indices))
	if len(scaling)==0:
		scaling=[1]*nPlots
	if method=="split": # break in x axis? https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/broken_axis.html
		fig,axs=plt.subplots(1,nPlots,sharey=True,gridspec_kw={"wspace":0,'width_ratios':scaling}) # 1 row, 2 columns, 0 spacing between the two, using ratios for sizing
		axs[0].spines['right'].set_visible(False) #; axs[1].spines['left'].set_visible(False) # get rid of extra spline and ticks
		axs[0].yaxis.tick_left() ; axs[1].yaxis.tick_right()
	if method=="stacked":
		fig,axs=plt.subplots(nPlots,sharex=True,gridspec_kw={"hspace":0,'height_ratios':scaling})
	if method=="shared":
		fig,ax1=plt.subplots() ; ax2=ax1.twinx() ; axs=[ax1,ax2]
	return axs,fig

def float2rgb(c): # float, 0 to 1
	#import matplotlib.cm as cm
	#return cm.inferno(1-c)[:3]		
	#return cm.rainbow(1-c)[:3]		
	return cmap(1-c)[:3]		

def processText(text): # automagically recognize things like "W m^-2 K^-1" and turn into the appropriate form: "W m$^{2}$ K$^{-1}$"
	terms=text.split()							# "TBC (W m^-2 K^-1)" --> ["TBC","(W","m^-2","K^-1)"]
	for i,t in enumerate(terms):
		if "^" in t:
			a,b=t.split("^")					# "K^-1)" --> ["K","-1)"]
			b1="".join( [c for c in b if c in "-0123456789." ] )	# only "-1" should be superscripted
			b2="".join( [c for c in b if c not in "-0123456789." ] ) # ")" should not be superscripted
			terms[i]=a+"$^{"+b1+"}$"+b2				# reassembled: "K$^{-1}$)"
	return " ".join(terms)

def setFace(fc): # https://stackoverflow.com/questions/19863368/how-to-change-the-legend-edgecolor-and-facecolor-in-matplotlib
	for ax,fr in zip(axs,frames):
		ax.set_facecolor(fc)
		fr.set_facecolor(fc)

def setLegendLW(lw):
	for fr in frames:
		fr.set_linewidth(lw)
