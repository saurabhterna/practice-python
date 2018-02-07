import osmnx as ox, networkx as nx


G = ox.graph_from_point((19.0213, 72.8424), distance=300, network_type='drive')

# define a lat-long point, create network around point, define origin/destination nodes
origin_node = list(G.nodes())[3]
destination_node = list(G.nodes())[8]
# find the route between these nodes then plot it

print(origin_node)

print(destination_node)


route = nx.shortest_path(G, origin_node, destination_node)
count = 0
for i in list(route):
  count += 1
print(count)
ox.plot_graph_route(G,route)
