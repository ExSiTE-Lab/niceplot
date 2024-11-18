import numpy as np
from niceplot import *
import sys

xs=np.linspace(0,10,20)
ys=xs**2

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


if 1 in tests:
	print("1")
	def ano(axs,fig):
		axs[0].annotate("A",xy=(xs[10],ys[10]),xytext=(xs[10],ys[10]+10),arrowprops={"facecolor":"black"})
	plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['k.','bo','r.'],title="annotations",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"],extras=[ano])

if 2 in tests:
	print("2")
	plot([xs]*14,[ys*.7,ys,ys/2,xs**3/2,xs**3/4,1/xs,xs,xs/2,xs/4,2*xs,np.sin(xs),np.cos(xs),np.sin(xs)*2,np.cos(xs)*2],title="check defMarks",xlabel="X",ylabel="Y")

if 3 in tests:
	print("3")
	plot([xs[10:],xs[10:],xs[10:]],[ys[10:]*.7,ys[10:],ys[10:]/2],markers=["r,o","b+","g-"],title="minorticks = True",xlabel="X",ylabel="Y",minorticks=True)

if 4 in tests:
	print("4")
	plot([xs[10:],xs[10:],xs[10:]],[ys[10:]*.7,ys[10:],ys[10:]/2],markers=["r,o","b+","g-"],title="minorticks = False",xlabel="X",ylabel="Y",minorticks=False)

if 5 in tests:
	print("5")
	plot([xs,xs+.1,xs+.3],[ys,ys/2,ys/4],ye=[10,np.random.random(20)*10,[np.random.random(20)*5,np.random.random(20)*10]],title="error bars, mixed, asymmetric",labels=["uniform","point-by-point","point-by-point, asymmetric"]) #; sys.exit()

if 6 in tests:
	print("6")
	plot([xs,xs+.1,xs+.2,xs+.3],[ys,ys/2,ys/3,ys/4],ye=[10,np.random.random(20)*10,[[10],[20]],[np.random.random(20)*5,np.random.random(20)*10]],title="error bars, mixed, asymmetric",labels=["uniform","point-by-point","uniform, asymmetric","point-by-point, asymmetric"]) #; sys.exit()

if 7 in tests:
	print("7")
	plot([xs],[ys],xe=[2],ye=[10],title="horizontal and vertical error bars")

if 8 in tests:
	print("8")
	x=np.asarray([0,1]) ; y=np.random.random(2) ; e=[1,[1,.5],[[1,1],[.5,.5]]]
	plot([x,x+.1,x+.2],[y,y*2,y*3],ye=e,title="error bars, CHECK OUR WARNING")

if 9 in tests:
	print("9")
	plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['w.','bo','r.'],title="invert colors",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"],extras=[invertPlotColors])

if 10 in tests:
	print("10")
	plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],ye=[10,np.linspace(5,20,10)],markers=['k.','bo','r.'],title="errorbars",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"])

if 11 in tests:
	print("11")
	plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],ye=[10,np.linspace(5,20,10)],markers=['k.','bo','r.'],title="errorbars-CSV",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",labels=["A","B","C"],filename="testing54.csv")

if 12 in tests:
	print("12")
	Xs,Ys,Ye,XLB,YLB,DLBS=readCSV("testing54.csv")
	print(Xs,Ys,Ye)
	plot(Xs,Ys,ye=Ye,markers=['k.','bo','r.'],title="readread CSV",xlabel=XLB,ylabel=YLB,labels=DLBS)

if 13 in tests:
	print("13")
	plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['k-','b-','r-'],title="savedAsCSV",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",filename="testing54.csv",labels=["A","B","C"])

if 14 in tests:
	print("14")
	plot([xs,xs[10:],xs[:15]],[ys,ys[10:]/2,ys[:15]/3],markers=['k-','b-','r-'],title="savedAsCSV",xlabel="x values",ylabel="TBC (W m^-2 K^-1)",filename="testing54.csv",labels=["A","B","C"])

if 15 in tests:
	print("15")
	plot([xs,xs,xs],[ys,ys/2,ys/3],title="cycler?",labels=["x^2","1/2*x^2","1/3*x^2"])
	plot([xs,xs,xs],[ys,ys/2,ys/3],title="cycler should have reset",labels=["x^2","1/2*x^2","1/3*x^2"])

if 16 in tests:
	print("16")
	plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['25,o','50,o','75,o'],title="markers=['25,o','50,o','75,o']",labels=["x^2","1/2*x^2","1/3*x^2"])

if 17 in tests:
	print("17")
	plot([xs,xs],[ys,ys/2],markers=['#882e2e,^'],title="red, defaulted",labels=["x^2","1/2*x^2"],figsize=(10,2),fontsize=10)

if 18 in tests:
	print("18")
	plot([xs,xs],[ys,ys/2],markers=['r'],title="red, defaulted, saved not shown",labels=["wow","oh no"],filename="out.png")

if 19 in tests:
	print("19")
	plot([xs],[ys],markers=['ko'],title="black o",yscale="log")

if 20 in tests:
	print("20")
	plot([xs,xs],[ys,ys/2],markers=['k-','b.'],title="regular black line, blue dots")
	plot([xs,xs],[ys,ys/2],markers=['k-','b.'],title="fat black line, blue dots",lw=7)

if 21 in tests:
	print("21")
	plot([xs[10:],xs[10:],xs[10:]],[ys[10:]*.7,ys[10:],ys[10:]/2],markers=["g",'k,f0','k,f0'],title="black filled",xlabel="X",ylabel="Y")

if 22 in tests:
	print("22")
	plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['k,f0','k,f0'],title="black filled",xlabel="X",ylabel="Y")

if 23 in tests:
	print("23")
	plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['g,fA','g,fA'],title="how do those units look?",xlabel="X",ylabel="TBC (W m^-2 K^-1)",xlim=[None,35])

if 24 in tests:
	print("24")
	plot([xs[10:],xs[10:]],[ys[10:],ys[10:]/2],markers=['tab:blue,f0','00,f0'],title="blue filled,logx",xlabel="X",ylabel="TBC (W m^-2 K^-1)",xscale="log")

if 25 in tests:
	print("25")
	plot([xs],[ys],markers=['tab:orange'],title="BIG orange default sym",ms=25)

if 26 in tests:
	print("26")
	plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="shared x axis",multiplot={"method":"shared","indices":[0,0,1]})

if 27 in tests:
	print("27")
	plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="stacked",multiplot={"method":"stacked","indices":[0,0,1]})

if 28 in tests:
	print("28")
	plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="split",multiplot={"method":"split","indices":[0,0,1]})

if 29 in tests:
	print("29")
	plot([xs,xs,xs],[ys,ys/2,ys/3],markers=['ro','bo','go'],title="split, 1:10",multiplot={"method":"split","indices":[0,0,1],"scaling":[1,10]})

if 30 in tests:
	print("30")
	plot([xs,xs],[ys,ys],markers=['k','b'],title="black and blue")

if 31 in tests:
	print("31")
	plot([xs,xs,xs,xs],[ys,ys,ys/2,ys/2],markers=['o','-',"^",":"],title="o, line, ^, :")

if 32 in tests:
	print("32")
	markers=[{"color":"red","marker":"o","linestyle":"-.","linewidth":1,"markersize":5},
		{"color":"#882e2e","marker":"^","linestyle":":","linewidth":3,"markersize":15}]
	plot([xs,xs],[ys,ys/2],markers=markers,title="full markers dicts",labels=["red,o,-.,lw=1,ms=5","blue,^,:,lw=3,ms=15"],facecolor="lightgray")

if 33 in tests:
	print("33")
	markers=[{"color":"red","linestyle":"-.","linewidth":1,"fill":"fABC","alpha":.1},
		{"fill":"fABC"},
		{"color":"green","linestyle":"-.","linewidth":1,"fill":"fDEF","alpha":.7},
		{"fill":"fDEF"}]
	plot([xs,xs,xs,xs],[ys,ys/2,-ys+max(ys),-ys/2+max(ys)],markers=markers,title="full markers dicts",labels=["red,a=0.1","","green,a=0.7"])

if 34 in tests:
	print("34")
	Xs=[] ; Ys=[] ; mkrs=[]
	for i in range(1,10):
		Xs.append(xs) ; Ys.append(ys/i)
		mkrs.append(str(i*10-1)+",-")
	plot(Xs,Ys,markers=mkrs,title="lines colored from inferno")
	plot(Xs,Ys,markers=mkrs,title="lines colored from turbo",cmap="turbo")

if 35 in tests:
	print("35")
	Xs=[ xs ]*100 ; ivals=np.arange(1,101) ; Ys=[ i*ys for i in ivals ] ; mkrs=rainbow(100)
	plot(Xs,Ys,addcbar=(ivals,cmap,"[A]*x^2","lin"),markers=mkrs,labels=['']*100,xlim=[0,10],ylim=[0,None])
	
if 36 in tests:
	print("36")
	plot([xs],[ys+100],ylim=["nonzero"],title="defeat 0 between ylims")