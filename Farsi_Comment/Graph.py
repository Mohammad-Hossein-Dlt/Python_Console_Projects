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

# حلقه زیر دیکشنری را ایجاد میکند که هر راس گراف کامل را به همراه همه راس های دیگر که به آن متصل هستند را نشان میدهد
# در این دیکشنری یال تکراری وجود دارد 

for i in vertex :
	c = list()
	for j in vertex :
		if i != j : c.append(j)
	total_graph[i] = c
# print(total_graph)

# حلقه زیر دیکشنری دیگری را ایجاد میکند که هر راس گراف کامل را به همراه همه راس های دیگر که به آن متصل هستند را نشان میدهد
# با این تفاوت که در این دیکشنری یال تکراری وجود ندارد 

z = 0
for i in vertex:
	for j in vertex[z:]:
		if i != j:
			total_graph[j] = list(set(total_graph[i]) & set(total_graph[j]))
			total_graph[j].sort()
	z+=1
# print(total_graph)

# حلقه زیر لیستی را ایجاد میکند که در آن همه یال های گراف کامل را بدون تکرار نشان میدهد

for i in vertex:
	if len(total_graph[i]) != 0 :
		for j in total_graph[i] :
			total_graph_edge.append([i , j])
# print(total_graph_edge)

# ---------------------------  پیدا کردن همه یال های گراف کامل روش دوم -----------------------

#  برای پیدا کردن تمام یال های گراف کامل این حلقه نسبت به سه حلقه بالا مشخصا کد کمتری دارد ولی سرعت آن از روش بالا کمتر است
# همچنین در روش اول برای پیدا کردن یال های گراف ترتیب خاصی بر اساس راس هایشان رعایت میشود که در این روش اتفاق نمی افتد


# while len(total_graph_edge) != vertex_number*(vertex_number-1)/2: 
# 	r = random.sample(vertex,2)
# 	r.sort()
# 	if r not in total_graph_edge and r[::-1] not in total_graph_edge : total_graph_edge.append(r)


# ------------------------------------------------------------------------------------------
# print(total_graph_edge , len(total_graph_edge))

#  دو متغیر و حلقه زیر برای محاسبه تعداد همه حالت های ممکن برای ایجاد گراف هایی با تعداد یال مشخص و تعداد راس مشخص
# مثلا تعداد گراف هایی با 5 راس و 3 یال برابر است با 120
p = [x for x in range(len(total_graph_edge)+1) if x != 0][::-1]
c = 1
for i in p[:Edge_number]: c = c*i
print(f"All Number Of Graph With {vertex_number} Vertex And {Edge_number} Edge:",c/math.factorial(Edge_number))
# C در حلقه زیر به کمک متغییر 
# به نوعی عمل انتخاب صورت گرفته است تا همه راس هایی از هر گراف که یالی به آن ها متصل شده است با رعایت ترتیب قرار گیری در قالب یک لیست به لیست بزرگتر اضافه شوند
# در واقع جواب نهایی حلقه زیر یک لیست بزرگ است که عضو های آن خود یک لیست هستند و نشان دهنده یک گراف از بین همه گراف های موجود است 
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
# تابعی برای فیلتر کردن راس ها یا مسیر های خاص در گراف کامل
def path(first_point , second_point , path_filter) :
	v = vertex
	v.remove(first_point)
	v.remove(second_point)
	path = [[first_point,second_point]]
	# به خاطر اینکه راس های قرار گرفته در مسیر بین دو راس مشخص شده میتوانند تعداد و جایگشت های مختلفی داشته باشند و تعداد و جایگشت های مختلف آن ها مسیر های متفاوت و جدیدی ایجاد میکند
	# حلقه زیر تمام این حالت ها را بررسی میکند
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
		# فیلتر بر اساس مسیر
		if path_filter[-1] == "path":
			path_filter.remove("path")
			for i in path_filter:
				for j in path:
					if "".join(i) in "".join(j) and j not in del_filter : del_filter.append(j)

		# فیلتر بر اساس راس 
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

# path("B","D" ,[["A","C"],"vertex"])


# این تابع لیستی را برمیگرداند که در آن بر اساس انتخاب کاربر راس ها یا یال هایی از گراف که قرار است حذف شوند قرار دارند
def vertex_or_path():
	select = input("ّFilter Vertex:'v' Path: 'p' Not_Filter(All path): 'e' \n").capitalize()
	filter_graph = list()
	if select == "E": filter_graph = []
	if select == "V" :
		filter_graph.append(set(input(f"Enter Vertex:\n").upper()))
		filter_graph.append("vertex")
	if select == "P":
			# در این قسمت چون ترتیب قرار گیری هر دو راس برای حذف یال بین آن ها مهم است ابتدا یک لیست خالی را اضافه کردیم سپس ار حلفه زیر استفاده کردیم
			# چون اگر از
			#  sort() یا متد set()
			# استفاده میکردیم ترتیب قرار گیری بهم میریخت 
			# مثلا ما میخواهیم در گراق مسیری که از
			# A به c
			# میگذرد حذف شود ولی مسیری که از 
			# C به A
			# میگذرد باقی بماند
		for i in range(0,int(input("How many Path?\n"))):
			filter_graph.append([])
			for j in list(input(f"Enter Path {i+1}:\n").upper()): 
				if j not in filter_graph[i]: filter_graph[i].append(j)
		filter_graph.append("path")
	return filter_graph

path(input("First_Point:\n").upper(),input("Second_Point:\n").upper(),vertex_or_path())

