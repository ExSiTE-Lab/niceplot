import numpy as np
from nicecontour import *
import sys



# WHICH TESTS SHOULD WE RUN
if len(sys.argv)==1:
	tests=np.arange(100)
else:
	tests=[]
	for v in sys.argv[1:]:
		if "-" in v:
			n1,n2=v.split("-")
			tests=tests+list(np.arange(int(n1),int(n2)+1))
		else:
			tests.append(int(v))



xs=np.linspace(-10,10,100)
ys=np.linspace(-10,10,99)
zs=xs[None,:]**2-10*np.sin(ys[:,None])

radii=np.sqrt(xs[None,:]**2+ys[:,None]**2)
Z=[ np.sin(xs[None,:])/2*np.ones((len(ys),len(xs))) , np.cos(ys[:,None])/2*np.ones((len(ys),len(xs))) , np.exp(-2*(radii)**2/5**2) ]
if 1 in tests:
	print("1")
	contour(ZNChannel(Z),xs,ys,heatOrContour="pix",title="transparent 3 channel, custom cbar",cbar_range=[-1,1],cbar_cmap=matplotlib.cm.seismic)

z=np.zeros((len(ys),len(xs))) ; spacing=2
for i in range(-11,12):
	for j in range(-11,12):
		r=np.sqrt(i**2+j**2)
		z+=np.exp(-((xs[None,:]-i*spacing)**2+(ys[:,None]-j*spacing)**2)/.25**2) * np.exp(-r**2/5**2)
if 2 in tests:
	print("2")
	contour(z,xs,ys,xlabel="x ($\\AA$)",ylabel="y ($\\AA$)",title="spacing = "+str(spacing)+" $\\AA$")

iz,kx,ky=fft2(z,xs,ys,maxk=1)
if 3 in tests:
	print("3")
	contour(np.absolute(iz),kx,ky, xlabel="kx ($\\AA$^-1)",ylabel="ky ($\\AA$^-1)", title="real space spacing = "+str(spacing)+" $\\AA$")

x=xs[None,:]*np.ones(99)[:,None] ; y=ys[:,None]*np.ones(100)[None,:]
z=colorwheel(x,y)
if 4 in tests:
	print("4")
	contour(z,xs,ys,heatOrContour="pix",title="colorwheel preview")

z_sin=np.exp(-2*(ys[:,None]-np.sin(xs[None,:]))**2/2**2)
z_cos=np.exp(-2*(xs[None,:]-np.cos(ys[:,None]))**2/2**2)
z_quad=np.exp(-2*(ys[:,None]-xs[None,:]**2)**2/3**2)
z_circ=np.exp(-2*(5**2-ys[:,None]**2-xs[None,:]**2)**2/8**2)
if 5 in tests:
	print("5")
	contour(roygbvr(z_sin),xs,ys,heatOrContour="pix")
if 6 in tests:
	print("6")
	contour(ZNChannel([z_sin,z_cos,z_quad,z_circ]),xs,ys,heatOrContour="pix",title="ZNChannel")
if 7 in tests:
	print("7")
	contour(Z3ChannelRGB([z_sin,z_cos,z_quad]),xs,ys,heatOrContour="pix",title="Z3ChannelRGB")
if 8 in tests:
	print("8")
	contour(Z3Channel([z_sin,z_cos,z_quad]),xs,ys,heatOrContour="pix",title="Z3Channel")
if 9 in tests:
	print("9")
	contour(Z3Channel([z_sin,z_cos,z_quad]),xs,ys,heatOrContour="pix",title="Z3Channel, invert",extras=[invertContourColors])
if 10 in tests:
	print("10")
	contour(z_sin,xs,ys,heatOrContour="pix",cmap="turbo",title="sinusoid")
if 11 in tests:
	print("11")
	contour(z_cos,xs,ys,heatOrContour="pix",cmap="rainbow",useLast=True,title="useLast=True") # TODO FAILS

# DATASET TESTING:
# RAGGED Z (list of lists, different-length rows), RAGGED X (list of lists, one list for each row), 1D Y (positioning of each row)
zs=[[0,1,3,2,4],[2,3,5,4,3,6],[2,3,4,4],[1,2,3],[3,4,5,6,7,1]]
xs=[[0,1,2,3,4],[-1,0,1,2,3,4],[0,1,2,3],[0,2,3],[-1,0,1,2,3,4]]
ys=[0,1,2,3,4]
if 12 in tests:
	print("12")
	contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="ragged")
if 13 in tests:
	print("13")
	contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="ragged, heat",flip="y",filename="heat.svg")
if 14 in tests:
	print("14")
	contour(zs,xs,ys,heatOrContour="pix",extras=[invertContourColors],title="ragged, pix",filename="pix.svg")


# NxM, N, M
xs=np.linspace(-10,10,99)
ys=np.linspace(-10,10,100)
zs=xs[None,:]**2-10*np.sin(ys[:,None])
if 15 in tests:
	print("15")
	contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="grids, heat, invert")
# 1D FOR ALL
zs=np.array(zs.flat) ; xs=xs[None,:]*np.ones(100)[:,None] ; xs=np.array(xs.flat) ; ys=ys[:,None]*np.ones(99)[None,:] ; ys=np.array(ys.flat)
if 16 in tests:
	print("16")
	contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="flattened, heat, invert")

# RAGGED BEHAVIOR, BUT WHAT IF EACH ROW IS THE SAME LENGTH? (still one x per z. just because len(row1)==len(row2) doesn't mean the vals are the same)
xs=np.linspace(-10,10,9)
ys=np.linspace(-10,10,10)
zs=xs[None,:]**2-10*np.sin(ys[:,None])
xs=xs[None,:]*np.ones(10)[:,None]
xs[0,:]=np.roll(xs[0,:],4)
#print("zs",zs) ; print("xs",xs) ; print("ys",ys)
ls=[":"]*30 ; ls[5]="-"
if 17 in tests:
	print("17")
	contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="technically ragged?")
if 18 in tests:
	print("18")
	contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="inverted color, heat")
if 19 in tests:
	print("19")
	contour(zs,xs,ys,heatOrContour="contour",extras=[invertContourColors],title="inverted color, contour",linecolor="inferno")
if 20 in tests:
	print("20")
	contour(zs,xs,ys,heatOrContour="heat,contour",extras=[invertContourColors],title="inverted color, both")
if 21 in tests:
	print("21")
	contour(zs,xs,ys,heatOrContour="pix,contour",cmap="viridis",title="both")
if 22 in tests:
	print("22")
	contour(zs,xs,ys,heatOrContour="heat,contour",linestyle=":",title="both, ls = :")
if 23 in tests:
	print("23")
	contour(zs,xs,ys,heatOrContour="pix,contour",linestyle=ls,linewidth=3,title="linestyle, linewidth")
if 24 in tests:
	print("24")
	contour(zs,xs,ys,heatOrContour="heat,contour",linestyle=ls,linecolor=["black"]*5+["red"]+["black"]*40,title="custom line colors") # TODO FAILS
if 25 in tests:
	print("25")
	contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis",title="contour, linestyle")
if 26 in tests:
	print("26")
	contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="inferno",useLast=True,title="contour, linestyle, uselast") # TODO FAILS


xs=np.linspace(-10,10,99)
ys=np.linspace(-10,10,100)
zs=xs[None,:]**2-10*np.sin(ys[:,None])
c=np.linspace(0,1,len(xs)) ; mkr='.'
ls=[":"]*30 ; ls[5]="-"

if 27 in tests:
	print("27")
	contour(zs,xs,ys, heatOrContour="contour",linestyle=ls,linecolor="viridis", overplot=[{"xs":xs,"ys":xs**3/100,"kind":"scatter","marker":mkr,"c":c}, {"xs":xs[::3],"ys":xs[::3]**2/10,"kind":"line","linestyle":"-","color":"black"}], title="scatter")

scatx=xs[::5] ; scaty=scatx**3/100
texts=[ str(np.round(x,1))+","+str(np.round(y,1)) for x,y in zip(scatx,scaty) ]
if 28 in tests:
	print("28")
	contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis", overplot=[{"xs":scatx,"ys":scaty,"kind":"scatter","marker":mkr,"c":"red"},{"xs":scatx+2,"ys":scaty+2,"kind":"text","text":texts,"fontsize":20}])

if 29 in tests:
	print("29")
	contour(zs,xs,ys,heatOrContour="both",filename="out1.svg")
if 30 in tests:
	print("30")
	contour(zs,xs,ys,heatOrContour="both",filename="out2.svg",zlim=[np.mean(zs)-np.std(zs),np.mean(zs)+np.std(zs)])
if 31 in tests:
	print("31")
	contour(zs,xs,ys,heatOrContour="both",filename="out3.svg",zlim=[np.mean(zs)-np.std(zs),None])
if 32 in tests:
	print("32")
	contour(zs,xs,ys,heatOrContour="both",filename="out4.svg",zlim=[0,None])

if 33 in tests:
	print("33")
	contour(zs,xs,ys,heatOrContour="both",filename="out_2DZ.svg")
