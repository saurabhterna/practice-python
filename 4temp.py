import networkx as net
import sys
sys.stdout = open('degreeoutput.txt','wt')
FielName="GraphData.txt"
Graphtype=net.DiGraph()  

G = net.read_edgelist(FielName, create_using=Graphtype, nodetype=int, data=(('weight',int),))


for x in G.nodes():
      print ("Node: ", x, " has total #degree: ",G.degree(x), " , In_degree: ", G.in_degree(x)," and out_degree: ", G.out_degree(x))


for u,v in G.edges():
      print ("Weight of Edge ("+str(u)+","+str(v)+")", G.get_edge_data(u,v))
      
     
