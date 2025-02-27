import numpy as np
from nicecontour import *

xs=np.linspace(-10,10,100)
ys=np.linspace(-10,10,99)
zs=xs[None,:]**2-10*np.sin(ys[:,None])

#radii=np.sqrt(xs[:,None]**2+ys[None,:]**2)
#Z=[ np.sin(xs[None,:])/2*np.ones(len(ys))[:,None] , np.cos(ys[:,None])/2*np.ones(len(xs))[None,:] , np.exp(-2*(radii)**2/5**2) ]
#contour(ZNChannel(Z),xs,ys,heatOrContour="pix",title="transparent 3 channel")

Z=np.load("Z_testing.npy") ; x=np.load("x_testing.npy") ; y=np.load("y_testing.npy")
contour(Z.T,x,y,heatOrContour="pix")
rZ,ky,kx=fft2(Z,y,x)
rrZ,y2,x2=fft2(rZ,ky,kx,inverse=True)
contour(np.absolute(rrZ).T,x2,y2,heatOrContour="pix")



z=np.zeros((len(ys),len(xs))) ; spacing=2
for i in range(-11,12):
	for j in range(-11,12):
		r=np.sqrt(i**2+j**2)
		z+=np.exp(-((xs[None,:]-i*spacing)**2+(ys[:,None]-j*spacing)**2)/.25**2) * np.exp(-r**2/5**2)
contour(z,xs,ys,xlabel="x ($\\AA$)",ylabel="y ($\\AA$)",title="spacing = "+str(spacing)+" $\\AA$")
iz,kx,ky=fft2(z,xs,ys,maxk=1)
contour(np.absolute(iz),kx,ky,xlabel="kx ($\\AA$^-1)",ylabel="ky ($\\AA$^-1)",title="real space spacing = "+str(spacing)+" $\\AA$")


x=xs[None,:]*np.ones(100)[:,None] ; y=ys[:,None]*np.ones(100)[None,:]
z=colorwheel(x,y)
contour(z,xs,ys,heatOrContour="pix",title="colorwheel preview")


#Z=1-np.absolute(ys[:,None]-np.sin(xs[None,:]))
z_sin=np.exp(-2*(ys[:,None]-np.sin(xs[None,:]))**2/2**2)
z_cos=np.exp(-2*(xs[None,:]-np.cos(ys[:,None]))**2/2**2)
z_quad=np.exp(-2*(ys[:,None]-xs[None,:]**2)**2/3**2)
z_circ=np.exp(-2*(5**2-ys[:,None]**2-xs[None,:]**2)**2/8**2)
#contour(roygbvr(z_sin),xs,ys,heatOrContour="pix")
contour(ZNChannel([z_sin,z_cos,z_quad,z_circ]),xs,ys,heatOrContour="pix",title="ZNChannel")
contour(Z3ChannelRGB([z_sin,z_cos,z_quad]),xs,ys,heatOrContour="pix",title="Z3ChannelRGB")
contour(Z3Channel([z_sin,z_cos,z_quad]),xs,ys,heatOrContour="pix",title="Z3Channel")
contour(Z3Channel([z_sin,z_cos,z_quad]),xs,ys,heatOrContour="pix",title="Z3Channel, invert",extras=[invertContourColors])
#contour(z_sin,xs,ys,heatOrContour="pix",cmap="turbo")
#contour(z_cos,xs,ys,heatOrContour="pix",cmap="rainbow",useLast=True)

# DATASET TESTING: 
# RAGGED Z (list of lists, different-length rows), RAGGED X (list of lists, one list for each row), 1D Y (positioning of each row)
zs=[[0,1,3,2,4],[2,3,5,4,3,6],[2,3,4,4],[1,2,3],[3,4,5,6,7,1]]
xs=[[0,1,2,3,4],[-1,0,1,2,3,4],[0,1,2,3],[0,2,3],[-1,0,1,2,3,4]]
ys=[0,1,2,3,4]
#contour(zs,xs,ys,heatOrContour="heat",extras=[invertColors],title="...")
contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="heat",flip="y",filename="heat.svg")
contour(zs,xs,ys,heatOrContour="pix",extras=[invertContourColors],title="pix",filename="pix.svg") ; sys.exit()
# NxM, N, M
xs=np.linspace(-10,10,99)
ys=np.linspace(-10,10,100)
zs=xs[None,:]**2-10*np.sin(ys[:,None])
#contour(zs,xs,ys,heatOrContour="heat",extras=[invertColors],title="...")
# 1D FOR ALL
zs=np.array(zs.flat) ; xs=xs[None,:]*np.ones(100)[:,None] ; xs=np.array(xs.flat) ; ys=ys[:,None]*np.ones(99)[None,:] ; ys=np.array(ys.flat)
#contour(zs,xs,ys,heatOrContour="heat",extras=[invertColors],title="...")
# RAGGED BEHAVIOR, BUT WHAT IF EACH ROW IS THE SAME LENGTH? (still one x per z. just because len(row1)==len(row2) doesn't mean the vals are the same)
xs=np.linspace(-10,10,9)
ys=np.linspace(-10,10,10)
zs=xs[None,:]**2-10*np.sin(ys[:,None])
xs=xs[None,:]*np.ones(10)[:,None]
xs[0,:]=np.roll(xs[0,:],4)
print("zs",zs) ; print("xs",xs) ; print("ys",ys)

contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="...")


contour(zs,xs,ys,heatOrContour="heat",extras=[invertContourColors],title="inverted color, heat")
contour(zs,xs,ys,heatOrContour="contour",extras=[invertContourColors],title="inverted color, contour",linecolor="inferno")
contour(zs,xs,ys,heatOrContour="both",extras=[invertContourColors],title="inverted color, both")

#contour(zs,xs,ys,heatOrContour="both",filename="out.svg")
contour(zs,xs,ys,heatOrContour="both",cmap="viridis")
#contour(zs,xs,ys,heatOrContour="both",linestyle=":")
ls=[":"]*30 ; ls[5]="-"
#contour(zs,xs,ys,heatOrContour="both",linestyle=ls,linewidth=3)
#contour(zs,xs,ys,heatOrContour="both",linestyle=ls,linecolor=["black"]*5+["red"]+["black"]*40)
contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis")
contour(zs.T,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="inferno",useLast=True)
mkr="." ; c=np.linspace(0,1,100)
#contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis",overplot=[{"xs":xs,"ys":xs**3/100,"kind":"scatter","marker":mkr,"c":c},{"xs":xs,"ys":xs**2/10,"kind":"line","linestyle":"-","color":"black"}])
scatx=xs[::5] ; scaty=scatx**3/100
texts=[ str(np.round(x,1))+","+str(np.round(y,1)) for x,y in zip(scatx,scaty) ]
#contour(zs,xs,ys,heatOrContour="contour",linestyle=ls,linecolor="viridis", overplot=[{"xs":scatx,"ys":scaty,"kind":"scatter","marker":mkr,"c":"red"},{"xs":scatx+2,"ys":scaty+2,"kind":"text","text":texts,"fontsize":20}])

#contour(zs,xs,ys,heatOrContour="both",filename="out1.svg")
#contour(zs,xs,ys,heatOrContour="both",filename="out2.svg",zlim=[np.mean(zs)-np.std(zs),np.mean(zs)+np.std(zs)])
#contour(zs,xs,ys,heatOrContour="both",filename="out3.svg",zlim=[np.mean(zs)-np.std(zs),None])
#contour(zs,xs,ys,heatOrContour="both",filename="out4.svg",zlim=[0,None])

contour(zs,xs,ys,heatOrContour="both",filename="out_2DZ.svg")
zs=np.asarray(zs.flat) ; xs=xs[None,:]*np.ones((100,100)) ; xs=np.asarray(xs.flat) ; ys=ys[:,None]*np.ones((100,100)) ; ys=np.asarray(ys.flat)
#print(np.shape(zs),np.shape(xs),np.shape(ys))
contour(zs,xs,ys,heatOrContour="both",filename="out_1DZ.svg")