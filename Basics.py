import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

## Scatter plots
# xd=np.random.random(1000)*100
# yd=np.random.random(1000)*100
# plt.scatter(xd,yd,c="purple",marker="*",s=50,alpha=0.3) #or hexcodes for colors and s is the size and alpha is basically the opacity for the markers that overlap with each other in the plot
# plt.show()

## Line plots
# years=[2000 + x for x in range(24)]
# weights=[73,90,79,79,88,77,86,77,90,77,88,83,74,73,74,90,70,74,71,79,85,76,84,88]
# plt.plot(years,weights,color="red",marker="*",alpha=0.8,lw=3,linestyle="--") #or "r--"
# plt.show()

## Bar plots
# x=["python","c++","c#","java","rust"]
# y=[60,70,10,60,5]
# plt.bar(x,y,color="red",align="edge",width=0.1,edgecolor="green",lw=2) #align would mean to align the marking on x axis and lw and edgecolor would mean the width of the edge and the color of the edge respc.
# plt.show()

## Histograms
# ages=np.random.normal(20,1.5,1000)
# plt.hist(ages,bins=[ages.min(),18,21,ages.max()],cumulative=True) #bins here would basically be grouping those with equal width and cumulative would mean to show decr to max number of repeated values
# plt.show()

## Pie chart
# langs=["Python","C++","C","Rust","Java"]
# votes=[50,60,30,10,15]
# e=[0,0.2,0,0,0] #used to show a section of the pie chart seperately
# plt.pie(votes, labels=langs, explode=e,autopct="%.2f%%",pctdistance=1.5,startangle=90) #autopct means to what precision and pctdistance is how far the pct from the label and finally startangle is from where the piechart should be started from
# plt.show()

## Box plots
# heights=np.random.normal(160,7.5,1000)
# plt.boxplot(heights) #for just basic understanding of boxplot
# fi=np.linspace(0,10,25)
# se=np.linspace(10,200,25)
# th=np.linspace(200,210,25)
# fo=np.linspace(210,230,25)
# data=np.concatenate((fi,se,th,fo),axis=0) 
# plt.boxplot(data) #used to understand how the bottom part of the boxplot is much farther away than the top part because as we can see, 0 to 10 range then se has 10 to 200
# plt.show()

## Plot customization
# years=[2014 + x for x in range(0,8)]
# income=[55,56,62,61,72,72,73,75]
# iticks=list(range(50,81,2)) #to label the values on the axes
# plt.plot(years,income)
# plt.title("Income of XXX",fontsize=10,fontname="8514oem") #windows key and type "fonts"
# plt.ylabel("Income")
# plt.xlabel("Years")
# plt.yticks(iticks,[f"${x}k" for x in iticks])
# plt.show()

## Legends and multiple plots
# d1=[100+ x for x in range(0,10)] #from here....
# d2=[103+ x for x in range(0,10)]
# d3=[107+ x for x in range(0,10)]
# plt.plot(d1,label="d1")
# plt.plot(d2,label="d2")
# plt.plot(d3,label="d3") #x value default as 0,1,...
# plt.legend(loc="lower right") #till here, its for line plot
# pets=["Mouse","Cat","Dog","Hamster","Parrot"] #from here...
# votes=[20,50,70,30,15]
# e=[0,0,0.2,0,0]
# plt.pie(votes,labels=pets,explode=e,autopct="%.2f%%",pctdistance=1.5) #typically we do this
# plt.pie(votes,labels=None) #but instead, this is done to use legend
# plt.legend(labels=pets,loc="lower right") #till here, its for pie plot
# plt.show()

## Plot styling
# style.use("ggplot") #different saturation
# style.use("dark_background")
# style.use("grayscale") #for more, check out the documentations: (i)https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html (ii)https://matplotlib.org/stable/users/explain/customizing.html
# pets=["Mouse","Cat","Dog","Hamster","Parrot"]
# votes=[20,50,70,30,15]
# plt.pie(votes,labels=pets)
# plt.show()

## Multiple figures
# x1,y1=np.random.random(100),np.random.random(100)
# x2,y2=np.random.random(100),np.random.random(100)
# plt.figure(1)
# plt.scatter(x1,y1)
# plt.figure(2)
# plt.plot(x2,y2)
# plt.show()

## Subplots 
# x=np.arange(1,101)
# fig,axs=plt.subplots(2,2) #00 01 10 11 and thus it creates a 2x2 grid (axs) with each cell of the grid containing the specific subplot and the whole figure is given by fig here
# axs[0,0].plot(x,np.sin(x))
# axs[0,0].set_title("Sine wave")
# axs[0,1].plot(x,np.cos(x))
# axs[0,1].set_title("Cosine wave")
# axs[1,0].plot(x,np.random.random(100))
# axs[1,0].set_title("Random function")
# axs[1,1].plot(x,np.log(x))
# fig.suptitle("Four different plots")
# plt.show()

## Exporting plots
# x=np.arange(1,101)
# f,a=plt.subplots(2,2)
# a[0,0].plot(x,np.sin(x))
# a[0,0].set_title("Sine wave")
# a[0,1].plot(x,np.cos(x))
# a[0,1].set_title("Cosine wave")
# a[1,0].plot(x,np.tan(x))
# a[1,0].set_title("Tangent wave")
# a[1,1].plot(x,np.log(x))
# a[1,1].set_title("Logarithmic function")
# f.suptitle("Four plots")
# plt.tight_layout() #avoids texts overlapping
# plt.savefig("fourplots.png",dpi=240,transparent=False,bbox_inches="tight",pad_inches=2) #higher dpi means higher quality and bbox_inches means the whitespace in the border

## 3D plotting
# t=plt.axes(projection="3d")
# x=np.random.random(100)
# y=np.random.random(100)
# z=np.random.random(100)
# t.set_title("3D graph")
# t.set_xlabel("Test1")
# t.set_ylabel("Test2")
# t.set_zlabel("Test3")
# # t.scatter(x,y,z)
# # t.plot(x,y,z)
# X,Y=np.meshgrid(x,y) #for 3d surfaces
# Z=np.sin(X)*np.cos(Y)
# t.plot_surface(X,Y,Z,cmap="Spectral")
# t.view_init(azim=0,elev=90) #initial view of the graph
# plt.show()

## Animating plots
# years=np.arange(1950,2021)
# pop=np.random.randint(100000,1000000,size=len(years))
# plt.title("Population over the years")
# plt.xlabel("Year")
# plt.ylabel("Population")
# for i in range(len(years)):
# plt.plot(years[:i],pop[:i],color="blue") #slicing upto i used to retain the previous plotting
# plt.pause(0.1) #essential for animating
# plt.show()
