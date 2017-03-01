## THIS CODE IS MODIFIED FROM SAMPLE CODE GIVEN IN
## DR. MATTHEW BERLAND'S COMPUTATIONAL RESEARCH METHODS COURSE (UW-MADISON)

from collections import Counter
import networkx as nx
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import csv

###OPEN CSV AND GET MARKOV SEQUENCE
csv_1 = csv.reader(open('/Users/catherinedornfeld/Desktop/CSCL_2017/SmallGroup/C5_C2_Sunfish_All.csv', 'rU'))
myList1 = []
next(csv_1) #skips header
for row in csv_1:
    myList1.append(row[1])
print myList1

###TRANSITION TABLES
observations = myList1  #[1,2,3,2,1,2,3,1,3,3,1,1,2] #dumb sample data
bigrams = zip(observations, observations[1:])
outlinks = Counter()
counts = Counter()
for elt in bigrams:
    counts[elt] += 1
    outlinks[elt[0]] += 1
mm = {elt: round(counts[elt]/float(outlinks[elt[0]]),2) for elt in counts}
print mm

###VISUALS
G = nx.DiGraph()
for edge in mm:
    G.add_edge(edge[0],edge[1],label=mm[edge])

##PROBLEM PIECE - may need to troubleshoot NetworkX
A=nx.nx_agraph.to_agraph(G)
A.graph_attr.update(dpi="800")
A.layout(prog="dot")
A.draw('VidyaMap_discourse.png') #change file name
#A.draw('/Users/catherinedornfeld/Desktop/All_Disc.svg') # -> need to change below, too

img=mpimg.imread('VidyaMap_discourse.png') #change file name
imgplot = plt.imshow(img)
plt.show()

