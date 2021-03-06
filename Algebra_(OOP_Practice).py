import os , math , matplotlib.pyplot as pl , numpy as np
os.system("cls")
""" Please enter the equations in the following format and make sure that there is no space between the equation sentences : ax^3 + bx^2 + cx + d
 x^3-4x^2+5x-2
 6x^3-4x^2-4x+2
 -6x^3+8x^2-4x+3
 -6x^3+8x^2-4x-3 
 x^3-4x+14
 2x^3-3x^2+6x+4
 x^3-4x^2+5x-2
 3x^3-3x^2+x+2 """
class equation_degrees2:
	def __init__(self,a__,b__,c__) :
		self.a = a__
		self.b = b__
		self.c = c__
		self.delta = self.b**2 - 4*self.a*self.c
		self.min_max = -self.b / (2*self.a)
		self.root = list()
		if self.delta>=0:
			self.x1=(-self.b+math.sqrt(self.delta)) / (2*self.a)
			self.x2=(-self.b-math.sqrt(self.delta)) / (2*self.a)
			self.root.append(self.x1)
			self.root.append(self.x2)
			self.root = list(set(self.root))
			self.root.sort()
	def RootInfo(self):
		print("Roots: " ,self.root)
		if self.delta>0:
			# a > 0
			# b and c != 0
			if self.a > 0 and self.b > 0 and self.c > 0 : return "The equation has 2(-) roots and The function diagram Do Not passes through area 4" # "معادله 2 ریشه (-) دارد . نمودار از ناحیه 4 نمیگذرد"
			elif self.a > 0 and self.b < 0 and self.c > 0 : return "The equation has 2 (+) roots and The function diagram Do Not passes through area 3" # "معادله 2 ریشه (+) دارد و نمودار از ناحیه 3 نمیگذزد"
			# a > 0
			# b or c == 0
			elif self.a > 0 and self.b > 0 and self.c == 0 : return "The equation has a (-) and a 0 roots and The function diagram Do Not passes through area 4" # "معادله 1 ریشه (-) و یک ریشه 0 دارد و نمودار از  ناحیه 4 نمیگذزد"
			elif self.a > 0 and self.b < 0 and self.c == 0 : return "The equation has a (+) and a 0 roots and The function diagram Do Not passes through area 3" #"معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از 3 ناحیه نمیگذزد"
			# a < 0
			elif self.a < 0 and self.b > 0 and self.c < 0 : return "The equation has 2 (+) roots and The function diagram Do Not passes through area 2" # "معادله 2 ریشه (+) دارد و نمودار از ناحیه 2 نمیگذزد"
			elif self.a < 0 and self.b < 0 and self.c < 0 : return "The equation has 2 (-) roots and The function diagram ِ Do Not passes through area 1" # "معادله 2 ریشه (-) دارد و نمودار از ناحیه 1 نمیگذزد"
			# a < 0
			# b or c == 0
			elif self.a < 0 and self.b > 0 and self.c == 0 : return "The equation has a (+) and a 0 roots and The function diagram Do Not passes through area 2" #"معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از  ناحیه 2 نمیگذزد"
			elif self.a < 0 and self.b < 0 and self.c == 0 : return "The equation has a (-) and a 0 roots and The function diagram Do Not passes through area 1" # "معادله 1 ریشه (-) و یک ریشه 0 دارد و نمودار از ناحیه 1 نمیگذزد"
			# 6 similar modes
			elif (self.a < 0 and self.b == 0 and self.c > 0) or (self.a < 0 and self.b < 0 and self.c > 0) or (self.a < 0 and self.b > 0 and self.c > 0) or (self.a > 0 and self.b == 0 and self.c < 0) or (self.a > 0 and self.b < 0 and self.c < 0) or (self.a > 0 and self.b>0 and self.c < 0) : return "The equation has a (+) and a (-) roots and The function diagram passes through All areas" # "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
		if self.delta == 0:
			if self.a > 0 and self.b > 0 and self.c > 0 : return "The equation has a (-) root and The function diagram passes through areas 1 and 2" # "معادله 1  (-) دارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif self.a > 0 and self.b < 0 and self.c > 0 : return "The equation has a (+) root and The function diagram passes through areas 1 and 2" # "معادله 1 ریشه (+) دارد و نمودار از 4 ناحیه میگذزد"
			elif self.a > 0 and self.b == 0 and self.c == 0 : return "The equation root is 0 and The function diagram passes through areas 1 and 2" # "معادله 1 ریشه 0 دارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif self.a < 0 and self.b == 0 and self.c == 0 : return "The equation root is 0 and The function diagram passes through areas 3 and 4" # "معادله 1 ریشه 0 دارد و نمودار از ناحیه 3 و 4 میگذزد"
			elif self.a < 0 and self.b > 0 and self.c < 0 : return "The equation has a (+) root and The function diagram passes through areas 3 and 4" # "معادله 1 ریشه (+) دارد و نمودار از ناحیه 3 و 4 میگذزد"
			elif self.a < 0 and self.b < 0 and self.c < 0 : return "The equation has (-) root and The function diagram passes through areas 3 and 4" # "معادله یک ریشه (-) دارد و نمودار از  ناحیه 3 و 4 میگذزد"
		elif self.delta < 0:
			if (self.a > 0 and self.b > 0 and self.c > 0) or (self.a > 0 and self.b < 0 and self.c > 0) or (self.a > 0 and self.b == 0 and self.c > 0) : return "The equation has no roots and The function diagram passes through areas 1 and 2" # "معادله ریشه ندارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif (self.a < 0 and self.b == 0 and self.c < 0) or (self.a < 0 and self.b > 0 and self.c < 0) or (self.a < 0 and self.b < 0 and self.c < 0) : return "The equation has no roots and The function diagram passes through areas 3 and 4" # "معادله ریشه ندارد و نمودار از  ناحیه 3 و 4 میگذزد"
	def diagram(self):
		pass
#-------------------------------------------------------------------------
class equation_degrees3:
	def __init__(self , ax3 , bx2 , cx , d , ex_x):
		self.ax3 = ax3/ax3
		self.bx2 = bx2/ax3
		self.cx = cx/ax3
		self.d = d/ax3
		self.p = self.cx - ((self.bx2**2)/3)
		self.q = (( 2 * ( self.bx2 ** 3 ) / 27 ) - (( self.bx2 * self.cx ) / 3)) + self.d
		self.delta = (( self.q**2 ) / 4 ) + (( self.p**3 ) / 27)
		self.roots = []
		self.ex_x = ex_x
		""" If 0 > Delta , equation has 3 roots 
                 If 0 = Delta , equation has 2 roots
                 If 0 < Delta , equation has 1 root """
		if len(ex_x) == 2:
			self.ex_y1 , self.ex_y2 = ax3 * ( ex_x[0] ** 3 ) + bx2*( ex_x[0] ** 2 ) + cx * ex_x[0] + d  ,  ax3 * ( ex_x[1] ** 3 ) + bx2*( ex_x[1] ** 2 ) + cx * ex_x[1] + d
			self.extermom = [(ex_x[0] , self.ex_y1) , (ex_x[1] , self.ex_y2)]
		if len(ex_x) == 1:
			self.ex_y =  ax3 * ( ex_x[0] ** 3 ) + bx2*( ex_x[0] ** 2 ) + cx * ex_x[0] + d
			self.extermom = [(ex_x[0], self.ex_y)]
		if len(ex_x) == 0:
			self.ex_y1 = self.ex_y2 = 0
			self.extermom = "Extermom Does Not Exist !!!!"
		equation_degrees3.roots__(self)
	def roots__(self):
		""" Delta can be used to determine the number of roots, but sometimes because of  being very close Delta to the number 0 by the negative and positive side , system rounds this number to 0
                 For example, the actual value of the delta may be a positive or negative number, but the system considers it to be 0
                 Function extermoms have been used to control and solve this problem """
		if (len(self.ex_x) != 2) or ( self.ex_y1 > 0 and self.ex_y2 > 0 ) or ( self.ex_y1 < 0 and self.ex_y2 < 0) or (self.ex_y1 == 0 and self.ex_y2 == 0)  :
			""" Because sometimes the number in the "pow()" method becomes negative and this method can only power positive numbers, we controlled this problem by defining 2 variables and the 2 following conditions.
                        Using the "pow()" method in this condition block and the low condition block is due to the square root of the 3, because the square method in the math library returns only the second root of the number. """
			n = m = 1
			if (-self.q/2 ) + math.sqrt(self.delta) < 0 : n = -n
			if (-self.q/2 ) - math.sqrt(self.delta) < 0 : m = -m
			x = ( n * math.pow(  n*( (-self.q/2 ) + math.sqrt(self.delta)) , 1/3 ) ) +  (  m * math.pow( m * (( -self.q/2 ) - math.sqrt(self.delta)) , 1/3 ) ) - (self.bx2/3)
			self.roots = [x]
			return f"Root: {round(x,4)}"
		if ( ( self.ex_y1 == 0 ) and ( self.ex_y2 < 0 or self.ex_y2 > 0)) or (( self.ex_y2 == 0 ) and ( self.ex_y1 < 0 or self.ex_y1 > 0)) :
			n = 1 # There is the problem of the previous in this part and we controlled in the same way
			if self.q < 0 : n = -1
			x1 = ( -2 * ( n * math.pow( n * self.q/2 , 1/3) ) ) - ( self.bx2 / 3)
			x2 = ( n * math.pow( n * self.q/2 , 1/3) ) - ( self.bx2 / 3 )
			self.roots = [x1,x2]
			self.roots.sort()
			return f"Roots:  {round(x1,4)} , {round(x2,4)}"
		if ( self.ex_y1 > 0 and self.ex_y2 < 0) or ( self.ex_y1 < 0 and self.ex_y2 > 0) :
			x =  (-2 / math.sqrt(3) ) * math.sqrt(-self.p) * math.sin( ( (math.asin( (3*math.sqrt(3)*self.q) / (2*(math.sqrt(-self.p)**3) ) ) ) / 3 ) + math.pi/3 ) - self.bx2/3
			x2 =  (2 / math.sqrt(3) ) * math.sqrt(-self.p) * math.sin( ( (math.asin( (3*math.sqrt(3)*self.q) / (2*(math.sqrt(-self.p)**3) ) ) ) / 3 ) ) - self.bx2/3
			x3 =  (2 / math.sqrt(3) ) * math.sqrt(-self.p) * math.cos( ( (math.asin( (3*math.sqrt(3)*self.q) / (2*(math.sqrt(-self.p)**3) ) ) ) / 3 ) + math.pi/6 ) - self.bx2/3
			self.roots = [x,x2,x3]
			self.roots.sort()
			return f"Roots:  {round(x,4)} , {round(x2,4)} , {round(x3,4)}"
	def diagram(self):
		if len(self.ex_x) == 2 :
			same_width = equation_degrees3(ax3, bx2, cx, d - eq3.ex_y1, self.ex_x)
			same_width2 = equation_degrees3(ax3, bx2, cx, d - eq3.ex_y2, self.ex_x)
			for i in self.ex_x: self.ex_x[self.ex_x.index(i)] = round(i, 4)
			for i in same_width.roots: same_width.roots[same_width.roots.index(i)] = round(i, 4)
			for i in same_width2.roots: same_width2.roots[same_width2.roots.index(i)] = round(i, 4)
			for i in self.ex_x:
				for j in [same_width.roots, same_width2.roots]:
					if i in j: j.remove(i)
			same_width_list = [same_width.roots[0], same_width2.roots[0]]
			same_width_list.sort()
		if len(self.roots) == 1:
			if len(self.ex_x) == 0 or len(self.ex_x) == 1:
				domain = [x for x in np.arange(self.roots[0] - abs(self.roots[0]), round(((-2 * bx2) / (6 * ax3)), 4) + 2 * abs(self.roots[0]),0.001)]
				domain.append(round(((-2 * bx2) / (6 * ax3)), 4) + 2 * abs(self.roots[0]))
				range = list(map(lambda x: ax3 * (x ** 3) + bx2 * (x ** 2) + cx * x + d, domain))
			if len(self.ex_x) == 2:
				print(self.roots)
				domain = [x for x in np.arange(self.roots[0], same_width_list[1], 0.001)]
				domain.append(same_width_list[1])
				range = list(map(lambda x: ax3 * (x ** 3) + bx2 * (x ** 2) + cx * x + d, domain))
		if len(self.roots) != 1:
			domain = [x for x in np.arange(same_width_list[0], same_width_list[1], 0.001)]
			domain.append(same_width_list[1])
			range = list(map(lambda x: ax3 * (x ** 3) + bx2 * (x ** 2) + cx * x + d, domain))
		pl.plot(domain, range , label = "Main Equation")
		pl.title("Equation Degrees 3 Diagram" , color = "Blue")
		pl.grid()
		if len(self.ex_x) == 2:
			domain2 = [x for x in np.arange(self.ex_x[0], self.ex_x[-1], 0.001)]
			# domain2 = [x for x in np.arange(self.roots[0], same_width_list[1], 0.001)]
			domain2.append(self.ex_x[-1])
			# domain2.append(same_width_list[1])
			range2 = list(map(lambda x: 3 * ax3 * (x ** 2) + 2 * bx2 * x + cx, domain2))
			pl.plot(domain2, range2 , label = "Derivative")
		if len(self.ex_x) == 1:
			domain2 = [x for x in np.arange(self.roots[0] - abs(self.roots[0]), round(((-2 * bx2) / (6 * ax3)), 4) + 2 * abs(self.roots[0]),0.001)]
			domain2.append(round(((-2 * bx2) / (6 * ax3)), 4) + 2 * abs(self.roots[0]))
			range2 = list(map(lambda x: 3 * ax3 * (x ** 2) + 2 * bx2 * x + cx, domain2))
			pl.plot(domain2, range2 , label = "Derivative")
		pl.ylabel("Range" , color = "Blue")
		pl.xlabel("Domain", color = "Blue")
		pl.legend()
		pl.show()
#-------------------------------------------------------------------------
equation = "".join(list(filter(lambda x : x !="", input("Enter Equation:\n").split(" ") ))) # We used this lambda function to remove extra distances
# At the bottom line , for easy separation of equation sentences and making a list of them we used replace() method to replace ("+" to " +") or ("-" to " -" )  to make the distance before the sign of each sentence , then we use split(" ") method
for i in [ ["X" , "x"] , ["**" , "^"] , ["+" , " +"] , ["-"," -"] , ["-x","-1x"] , ["+x","+1x"] ] : equation = equation.replace(i[0],i[1])
equation = list(filter(lambda x : x!="" , equation.split(" ")))
if equation[0][:equation[0].index("x")] == "" : equation[0] = equation[0].replace("x","+1x")
ax3 = sum(list(map( lambda x : int(x[:x.index("x^3")]) , list(filter(lambda x : "x^3" in x , equation)) )))
bx2 = sum(list(map( lambda x : int(x[:x.index("x^2")]) , list(filter(lambda x : "x^2" in x , equation)) )))
cx = sum(list(map( lambda x : int(x[:x.index("x")]) , list(filter(lambda x : ( "^"  not in x) and ("x" in x) , equation)) )))
d = sum(list(map(  lambda x : int(x) , list(filter(lambda x : "x" not in x , equation))   )))
if ax3 == 0:
	eq2 = equation_degrees2(bx2,cx,d)
	print(eq2.RootInfo())
	if bx2>0: print("Max: ", eq2.min_max)
	else: print("Min: ", eq2.min_max)
	roots = eq2.root
	roots.sort()
else :
	Derivative = equation_degrees2(3*ax3,2*bx2,cx)
	eq3 = equation_degrees3(ax3,bx2,cx,d , Derivative.root)
	print(eq3.roots__())
	print("Extermom's: " ,eq3.extermom)
	eq3.diagram()
