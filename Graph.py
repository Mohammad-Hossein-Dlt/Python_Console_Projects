import random , math , os
os.system("Cls")
vertex_number = int(input("Set Vertex Number: "))
print("All Number Of Edge : ",vertex_number*(vertex_number-1)/2,"\nYou Can Have A Graph Whith 0 To",vertex_number*(vertex_number-1)/2,"Edge's")
Edge_number = int(input("Set Edge Number: "))
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
vertex = alphabet[:vertex_number]
total_graph = dict()
total_graph_edge = list()
graph_edge = list()
# ---------------------------  پیدا کردن همه یال های گراف کامل روش اول -----------------------

# The following loop creates a dictionary that shows each vertex of the complete graph with all the other vertices that are connected to it 
# In this dictionary there is duplicate edges

for i in vertex :
	c = list()
	for j in vertex :
		if i != j :
			c.append(j)
	total_graph[i] = c

# The following loop creates another dictionary that shows each vertex of the complete graph with all the other vertices that are connected to it
# With the difference that there is no duplicate edges in this dictionary

z = 0
for i in vertex:
	for j in vertex[z:]:
		if i != j:
			total_graph[j] = list(set(total_graph[i]) & set(total_graph[j]))
			total_graph[j].sort()
	z+=1

# The following loop creates a list that shows all the edges of the complete graph without duplication

for i in vertex:
	if len(total_graph[i]) != 0 :
		for j in total_graph[i] :
			total_graph_edge.append([i , j])

# ---------------------------  پیدا کردن همه یال های گراف کامل روش دوم -----------------------

# To find all the edges of a complete graph, this loop has obviously less code than the above three loops, but its speed is lower than the above method
# Also, in the first method to find the edges of the graph, a special order is observed based on their vertices, which does not happen in this method

# while len(total_graph_edge) != vertex_number*(vertex_number-1)/2: 
# 	r = random.sample(vertex,2)
# 	r.sort()
# 	if r not in total_graph_edge and r[::-1] not in total_graph_edge : total_graph_edge.append(r)

# ------------------------------------------------------------------------------------------

# Two variables and the following loop to calculate the number of all possible modes to create graphs with a certain number of edges and a certain number of vertices
# For example, the number of graphs with 5 vertices and 3 edges is equal to 120

p , c = [x for x in range(len(total_graph_edge)+1) if x != 0][::-1] , 1
for i in p[:Edge_number]: c = c*i
print(f"All Number Of Graph With {vertex_number} Vertex And {Edge_number} Edge:",c/math.factorial(Edge_number))

# In the following loop The selection operation (in mathematics) is performed, so that all vertices of each graph with the edges connected to it, in the order of placement, are added to the larger list in the form of a list.
# In fact, the final answer of the loop below is a large list whose members are a list and represent a graph from all available graphs.

while len(graph_edge) != c/math.factorial(Edge_number) :
	random_vertex = random.sample(total_graph_edge,Edge_number)
	if len(graph_edge) == 0:
		graph_edge.append(random_vertex)
	else:
		x = 0
		for i in graph_edge:
			z = 0
			for j in random_vertex:
				if j not in i: z +=1
			if z != 0: x+=1
		if x == len(graph_edge): graph_edge.append(random_vertex)
for i in graph_edge:print(i)
#-------------------------------------------
# Function to filter specific vertices or paths in a complete graph
def path(first_point , second_point , path_filter) :
	v = vertex
	v.remove(first_point)
	v.remove(second_point)
	path = [[first_point,second_point]]
        # Because the vertices located in the path between the two specified vertices can have different numbers and permutations, and their different number and permutations create different and new paths
        # The following loop examines all of these modes
	for i in range(1,len(v)+1):
		z = len(v)
		for j in range(1,i): z = z*(len(v)-j) 
		s = 0
		while s != z :
			new_path = [first_point] + random.sample(v,i) +[second_point]
			if new_path not in path :
				path.append(new_path)
				s+=1
	
	del_filter = []
	if len(path_filter) != 0:
		# Filter by path
		if path_filter[-1] == "path":
			path_filter.remove("path")
			for i in path_filter:
				for j in path:
					if "".join(i) in "".join(j) and j not in del_filter : del_filter.append(j)

		# Filter by vertex
		if path_filter[-1] == "vertex":
			for i in path_filter[0]:
				for j in path:
					if i in j and j not in del_filter: del_filter.append(j)
	print(f"\nNumber Of All Path: {len(path)}" , f"All Path Between '{first_point}' and '{second_point}' :")
	for i in path: print(" > ".join(i))
	if len(del_filter) != 0:
		print("\n\nFiltred Path: ")
		for i in del_filter : print(" > ".join(i))
		for i in del_filter : path.remove(i)
		print(f"\n\nNumber Of All Path With Filter: {len(path)} ",f"All Path Between '{first_point}' and '{second_point}' With Filter:")
		for i in path: print(" > ".join(i))
#-------------------------------------------
# This function returns a list containing the vertices or edges of the graph to be deleted based on the user's choice
def vertex_or_path():
	select = input("ّFilter Vertex:'v' Path: 'p' Not_Filter(All path): 'e' \n").capitalize()
	filter_graph = list()
	if select == "E":
		filter_graph = []
	if select == "V" :
		filter_graph.append(set(input(f"Enter Vertex:\n").upper()))
		filter_graph.append("vertex")
	if select == "P":
                # In this section, because the order of placement of both vertices is important to remove the edge between them, first we added an empty list, then we used the following loop, because if we used "sort()" or "set()" method, the order of placement would be messd
                # For example, we want the path from A to C Can be deleted but the path from C to A Passes to stay
		for i in range(0,int(input("How many Path?\n"))):
			filter_graph.append([])
			for j in list(input(f"Enter Path {i+1}:\n").upper()):
				if j not in filter_graph[i]: filter_graph[i].append(j)
		filter_graph.append("path")
	return filter_graph

path(input("First_Point:\n").upper(),input("Second_Point:\n").upper(),vertex_or_path())
