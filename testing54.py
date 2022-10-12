import numpy as np
from niceplot import *

xs=np.linspace(0,10,20)
ys=xs**2

plot([xs,xs],[ys,ys/2],markers=['#882e2e,^'],title="red, defaulted",labels=["x^2","1/2*x^2"],figsize=(10,2),fontsize=10)
plot([xs,xs],[ys,ys/2],markers=['r'],title="red, defaulted",labels=["wow","oh no"])
plot([xs],[ys],markers=['ko'],title="black o")
plot([xs,xs],[ys,ys/2],markers=['k-','b.'],title="black line, blue dots")
plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['k,f0','k,f0'],title="black filled",xlabel="X",ylabel="Y")
plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['g,fA','g,fA'],title="how do those units look?",xlabel="X",ylabel="TBC (W m^-2 K^-1)",xlim=[None,35])
plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['tab:blue,f0','00,f0'],title="blue filled,logx",xlabel="X",ylabel="TBC (W m^-2 K^-1)",xscale="log")
plot([xs],[ys],markers=['tab:orange'],title="orange default sym")
plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="shared x axis",multiplot={"method":"shared","indices":[0,0,1]})
plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="stacked",multiplot={"method":"stacked","indices":[0,0,1]})
plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="split",multiplot={"method":"split","indices":[0,0,1]})
plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="split, 1:10",multiplot={"method":"split","indices":[0,0,1],"scaling":[1,10]})

plot([xs,xs],[ys,ys],markers=['k','b'],title="black and blue")
plot([xs,xs,xs,xs],[ys,ys,ys/2,ys/2],markers=['o','-',"^",":"],title="o, line, ^, :")

markers=[{"color":"red","marker":"o","linestyle":"-.","linewidth":1,"markersize":5},
	{"color":"#882e2e","marker":"^","linestyle":":","linewidth":3,"markersize":15}]
plot([xs,xs],[ys,ys/2],markers=markers,title="full markers dicts",labels=["red,o,-.,lw=1,ms=5","blue,^,:,lw=3,ms=15"],facecolor="lightgray")

markers=[{"color":"red","linestyle":"-.","linewidth":1,"fill":"fABC","alpha":.1},
	{"fill":"fABC"},
	{"color":"green","linestyle":"-.","linewidth":1,"fill":"fDEF","alpha":.7},
	{"fill":"fDEF"}]
plot([xs,xs,xs,xs],[ys,ys/2,-ys+max(ys),-ys/2+max(ys)],markers=markers,title="full markers dicts",labels=["red,a=0.1","","green,a=0.7"])

Xs=[] ; Ys=[] ; mkrs=[]
for i in range(1,10):
	Xs.append(xs) ; Ys.append(ys/i)
	mkrs.append(str(i*10-1)+",-")
plot(Xs,Ys,markers=mkrs,title="lines colored from inferno")