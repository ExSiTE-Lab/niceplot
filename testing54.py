import numpy as np
from niceplot import *
import sys

xs=np.linspace(0,10,20)
ys=xs**2

#def ano(axs,fig):
#	axs[0].annotate("A",xy=(xs[10],ys[10]),xytext=(xs[10],ys[10]+10),arrowprops={"facecolor":"black"})
#plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['k.','bo','r.'],title="annotations",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"],extras=[ano])

plot([xs,xs+.1,xs+.3],[ys,ys/2,ys/4],ye=[10,np.random.random(20)*10,[np.random.random(20)*5,np.random.random(20)*10]],title="error bars, mixed, asymmetric",labels=["uniform","point-by-point","point-by-point, asymmetric"]) #; sys.exit()

plot([xs,xs+.1,xs+.2,xs+.3],[ys,ys/2,ys/3,ys/4],ye=[10,np.random.random(20)*10,[[10],[20]],[np.random.random(20)*5,np.random.random(20)*10]],title="error bars, mixed, asymmetric",labels=["uniform","point-by-point","uniform, asymmetric","point-by-point, asymmetric"]) #; sys.exit()

plot([xs],[ys],xe=[2],ye=[10],title="horizontal and vertical error bars")

#xs=np.asarray([0,1]) ; ys=np.random.random(2) ; ye=[1,[1,.5],[[1,1],[.5,.5]]]
#plot([xs,xs+.1,xs+.2],[ys,ys*2,ys*3],ye=ye,title="error bars, CHECK OUR WARNING") ; sys.exit()

#plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['w.','bo','r.'],title="invert colors",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"],extras=[invertColors])


#plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],ye=[10,np.linspace(5,20,10)],markers=['k.','bo','r.'],title="errorbars",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"])
#plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],ye=[10,np.linspace(5,20,10)],markers=['k.','bo','r.'],title="errorbars-CSV",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"],filename="testing54.csv")
Xs,Ys,Ye,XLB,YLB,DLBS=readCSV("testing54.csv")
#print(Xs,Ys,Ye)
#plot(Xs,Ys,ye=Ye,markers=['k.','bo','r.'],title="readread CSV",xlabel=XLB,ylabel=YLB,labels=DLBS)




#plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['k-','b-','r-'],title="savedAsCSV",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",filename="testing54.csv",labels=["A","B","C"])

#plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['k-','b-','r-'],title="savedAsCSV",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",filename="testing54.csv",labels=["A","B","C"])

#plot([xs,xs,xs],[ys,ys/2,ys/3],title="cycler?",labels=["x^2","1/2*x^2","1/3*x^2"])
#plot([xs,xs,xs],[ys,ys/2,ys/3],title="cycler?",labels=["x^2","1/2*x^2","1/3*x^2"])

#plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['25,o','50,o','75,o'],title="markers=['25,o','50,o','75,o']",labels=["x^2","1/2*x^2","1/3*x^2"])
#plot([xs,xs],[ys,ys/2],markers=['#882e2e,^'],title="red, defaulted",labels=["x^2","1/2*x^2"],figsize=(10,2),fontsize=10)
#plot([xs,xs],[ys,ys/2],markers=['r'],title="red, defaulted, saved not shown",labels=["wow","oh no"],filename="out.png")
#plot([xs],[ys],markers=['ko'],title="black o",yscale="log")
#plot([xs,xs],[ys,ys/2],markers=['k-','b.'],title="black line, blue dots",lw=7)
plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['k,f0','k,f0'],title="black filled",xlabel="X",ylabel="Y")
#plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['g,fA','g,fA'],title="how do those units look?",xlabel="X",ylabel="TBC (W m^-2 K^-1)",xlim=[None,35])
plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['tab:blue,f0','00,f0'],title="blue filled,logx",xlabel="X",ylabel="TBC (W m^-2 K^-1)",xscale="log")
plot([xs],[ys],markers=['tab:orange'],title="orange default sym",ms=25)
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