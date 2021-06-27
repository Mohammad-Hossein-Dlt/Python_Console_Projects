import os , math
os.system("cls")
# Please enter the equations in the following format and make sure that there is no space between the equation sentences
# x**3-4x**2+5x-2
# 6x**3-4x**2-4x+2
# -6x**3+8x**2-4x+3
# -6x**3+8x**2-4x-3 
# x**3-4x+14
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
			self.root.append(round(self.x1,4))
			self.root.append(round(self.x2,4))
	def RootInfo(self):
		print("Roots: " ,self.root)
		if self.delta>0:
			# a>0
			# b,c!=0
			if self.a>0 and self.b>0 and self.c>0: return "The equation has 2(-) roots and The function diagram Do Not passes through area 4" # "معادله 2 ریشه (-) دارد . نمودار از ناحیه 4 نمیگذرد"
			elif self.a>0 and self.b>0 and self.c<0: return "The equation has a (-) root and a (+) root and The function diagram passes through All areas" # "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
			elif self.a>0 and self.b<0 and self.c>0: return "The equation has 2(+) roots and The function diagram Do Not passes through area 3" # "معادله 2 ریشه (+) دارد و نمودار از ناحیه 3 نمیگذزد"
			elif self.a>0 and self.b<0 and self.c<0: return "The equation has 2(-) roots and The function diagram passes through All areas" # "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
			# a>0
			# b,c==0
			elif self.a>0 and self.b==0 and self.c==0: return "The equation root is 0 and The function diagram passes through area 1 and 2" # "ریشه معادله 0 است و نمودار از ناحیه 1 و 2 میگذزد"
			elif self.a>0 and self.b>0 and self.c==0: return "The equation has a (-) and a 0 root and The function diagram Do Not passes through area 4" # "معادله 1 ریشه (-) و یک ریشه 0 دارد و نمودار از  ناحیه 4 نمیگذزد"
			elif self.a>0 and self.b<0 and self.c==0: return "The equation has a (+) and a 0 roo and The function diagram Do Not passes through area 3" #"معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از 3 ناحیه نمیگذزد"
			elif self.a>0 and self.b==0 and self.c<0: return "The equation has a (+) and (-) root and The function diagram passes through All areas" # "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
			#a<0
			elif self.a<0 and self.b>0 and self.c>0: return "The equation has a (+) and (-) root and The function diagram passes through All areas" # "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
			elif self.a<0 and self.b>0 and self.c<0: return "The equation has 2 (+) roots and The function diagram Do Not passes through area 2" # "معادله 2 ریشه (+) دارد و نمودار از ناحیه 2 نمیگذزد"
			elif self.a<0 and self.b<0 and self.c>0: return "The equation has a (+) and (-) root and The function diagram passes through All areas" # "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
			elif self.a<0 and self.b<0 and self.c<0: return "The equation has 2 (-) root and The function diagram ِ Do Not passes through area 1" # "معادله 2 ریشه (-) دارد و نمودار از ناحیه 1 نمیگذزد"
			#a<0
			# b,c==0
			elif self.a<0 and self.b==0 and self.c==0: return "The equation has a (+) and 0 root and The function diagram passes through area 3 and 4" # "معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از  ناحیه 3 و 4 میگذزد"
			elif self.a<0 and self.b>0 and self.c==0: return "The equation has a (+) 0 root and The function diagram passes Do Not through area 2" #"معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از  ناحیه 2 نمیگذزد"
			elif self.a<0 and self.b<0 and self.c==0: return "The equation has and (-) and 0 roots and The function diagram Do Not passes through area 1" # "معادله 1 ریشه (-) و یک ریشه 0 دارد و نمودار از ناحیه 1 نمیگذزد"
			elif self.a<0 and self.b==0 and self.c>0:return "The equation has a (+) and (-) root and The function diagram passes through All areas" # "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
		if self.delta == 0:
			if self.a>0 and self.b>0 and self.c>0 : return "The equation has a (-) root and The function diagram passes through areas 1 and 2" # "معادله 1  (-) دارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif self.a>0 and self.b<0 and self.c>0 : return "The equation has a (+) root and The function diagram passes through areas 1 and 2" # "معادله 1 ریشه (+) دارد و نمودار از 4 ناحیه میگذزد"
			elif self.a>0 and self.b==0 and self.c==0 : return "The equation root is 0 and The function diagram passes through areas 1 and 2" # "معادله 1 ریشه 0 دارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif self.a<0 and self.b==0 and self.c==0 : return "The equation root is 0 and The function diagram passes through areas 3 and 4" # "معادله 1 ریشه 0 دارد و نمودار از ناحیه 3 و 4 میگذزد"
			elif self.a<0 and self.b>0 and self.c<0 : return "The equation has a (+) root and The function diagram passes through areas 3 and 4" # "معادله 1 ریشه (+) دارد و نمودار از ناحیه 3 و 4 میگذزد"
			elif self.a<0 and self.b<0 and self.c<0 : return "The equation has (-) root and The function diagram passes through areas 3 and 4" # "معادله یک ریشه (-) دارد و نمودار از  ناحیه 3 و 4 میگذزد"
		elif self.delta < 0:
			if self.a>0 and self.b>0 and self.c>0 : return "The equation has no roots and The function diagram passes through areas 1 and 2" # "معادله ریشه ندارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif self.a>0 and self.b<0 and self.c>0 : return "The equation has no roots and The function diagram passes through areas 1 and 2" # "معادله ریشه ندارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif self.a>0 and self.b==0 and self.c>0 : return "The equation has no roots and The function diagram passes through areas 1 and 2" # "معادله ریشه ندارد و نمودار از  ناحیه 1 و 2 میگذزد"
			elif self.a<0 and self.b==0 and self.c<0 : return "The equation has no roots and The function diagram passes through areas 3 and 4" # "معادله ریشه ندارد و نمودار از  ناحیه 3 و 4 میگذزد"
			elif self.a<0 and self.b>0 and self.c<0 : return "The equation has no roots and The function diagram passes through areas 3 and 4" # "معادله ریشه ندارد و نمودار از  ناحیه 3 و 4 میگذزد"
			elif self.a<0 and self.b<0 and self.c<0 : return "The equation has no roots and The function diagram passes through areas 3 and 4" # "معادله ریشه ندارد و نمودار از  ناحیه 3 و 4 میگذزد"
#-------------------------------------------------------------------------
class equation_degrees3:
	def __init__(self , ax3 , bx2 , cx , d , ex):
		self.ax3 = ax3/ax3
		self.bx2 = bx2/ax3
		self.cx = cx/ax3
		self.d = d/ax3
		self.p = self.cx - ((self.bx2**2)/3)
		self.q = (( 2 * ( self.bx2 ** 3 ) / 27 ) - (( self.bx2 * self.cx ) / 3)) + self.d
		self.delta = (( self.q**2 ) / 4 ) + (( self.p**3 ) / 27)
		# "If 0 > Delta has 3 roots equation"
                # "If 0 = Delta has 2 roots in the equation"
                # "If 0 < delta has the root equation 1
		if len(ex) != 0:
			self.ex1 = ax3 * ( ex[0] ** 3 ) + bx2*( ex[0] ** 2 ) + cx * ex[0] + d
			self.ex2 = ax3 * ( ex[1] ** 3 ) + bx2*( ex[1] ** 2 ) + cx * ex[1] + d
			self.extermom = [(ex[0] , round(self.ex1,4)) , (ex[1] , round(self.ex2,4))]
		else:
			self.ex1 = self.ex2 = 0
			self.extermom = "Extermom Does Not Exist !!!!"
	def roots(self):
		# Delta can be used to determine the number of roots, but sometimes because of  being very close Delta to the number 0 by the negative and positive side , system rounds this number
                # For example, the actual value of the delta may be a positive or negative number, but the system considers it to be 0
                # Function extermoms have been used to control and solve this problem to a large extent
		if (( self.ex1 > 0 and self.ex2 > 0 ) or ( self.ex1 < 0 and self.ex2 < 0) ) or (self.ex1 == 0 and self.ex2 == 0) :
			# Because sometimes the number in the "pow()" method becomes negative and this method can only power positive numbers, we controlled this problem by defining 2 variables and the 2 following conditions.
                        # Using the "pow()" method in this condition block and the low condition block is due to the square root of the 3, because the square method in the math library returns only the second root of the number.
			n = m = 1
			if (-self.q/2 ) + math.sqrt(self.delta) < 0 : n = -n
			if (-self.q/2 ) - math.sqrt(self.delta) < 0 : m = -m
			x = ( n * math.pow(  n*( (-self.q/2 ) + math.sqrt(self.delta)) , 1/3 ) ) +  (  m * math.pow( m * (( -self.q/2 ) - math.sqrt(self.delta)) , 1/3 ) ) - (self.bx2/3)
			print("Root: " , round(x,4))
		if ( ( self.ex1 == 0 ) and ( self.ex2 < 0 or self.ex2 > 0)) or (( self.ex2 == 0 ) and ( self.ex1 < 0 or self.ex1 > 0)) :
			# There is the problem of the previous in this part and we controlled in the same way
			n = 1
			if self.q < 0 : n = -1
			x1 = ( -2 * ( n * math.pow( n * self.q/2 , 1/3) ) ) - ( self.bx2 / 3)
			x2 = ( n * math.pow( n * self.q/2 , 1/3) ) - ( self.bx2 / 3 )
			print("Roots: ",round(x1,4) , round(x2,4))
		if ( self.ex1 > 0 and self.ex2 < 0) or ( self.ex1 < 0 and self.ex2 > 0) :
			x =  (-2 / math.sqrt(3) ) * math.sqrt(-self.p) * math.sin( ( (math.asin( (3*math.sqrt(3)*self.q) / (2*(math.sqrt(-self.p)**3) ) ) ) / 3 ) + math.pi/3 ) - self.bx2/3
			x2 =  (2 / math.sqrt(3) ) * math.sqrt(-self.p) * math.sin( ( (math.asin( (3*math.sqrt(3)*self.q) / (2*(math.sqrt(-self.p)**3) ) ) ) / 3 ) ) - self.bx2/3
			x3 =  (2 / math.sqrt(3) ) * math.sqrt(-self.p) * math.cos( ( (math.asin( (3*math.sqrt(3)*self.q) / (2*(math.sqrt(-self.p)**3) ) ) ) / 3 ) + math.pi/6 ) - self.bx2/3
			print("Roots: ",round(x,4) , round(x2,4) , round(x3,4))
#-------------------------------------------------------------------------
equation = str(input("Enter Equation:\n"))
#To make a list of equation sentences when there is no space between the sentences, we used the following loop to make the distance, before the sign of that sentence , based on being sentens positive or negative
for i in ["+","-"] : equation = equation.replace(i,f" {i}")
equation = equation.split(" ")
if '' in equation : equation.remove('')
# To recognize "1" and "1" in "x.." , "-x.." We used the following loops and conditions
for i in equation :
	if "x" in i :
		if i[:i.index("x")] == "-": equation[equation.index(i)] = i.replace("-","-1")
		if i[:i.index("x")] == "+": equation[equation.index(i)] = i.replace("+","+1")
		if i[:i.index("x")] == "": equation[equation.index(i)] = "+1"+i
ax3 = sum(list(map(  lambda x : int(x[:x.index("x**3")]) , list(filter(lambda x : "x**3" in x , equation))  )))
bx2 = sum(list(map(  lambda x : int(x[:x.index("x**2")]) , list(filter(lambda x : "x**2" in x , equation))  )))
cx = sum(list(map(  lambda x : int(x[:x.index("x")]) , list(filter(lambda x : ( "**"  not in x) and ("x" in x) , equation))  )))
d = sum(list(map(   lambda x : int(x) , list(filter(lambda x : "x" not in x , equation))   )))
if ax3 == 0:
	Algebrax2 = equation_degrees2(bx2,cx,d)
	print(Algebrax2.RootInfo())
	if bx2>0:
		print("Max: ", Algebrax2.min_max)
	else:
		print("Min: ", Algebrax2.min_max)
else :
	Derivative = equation_degrees2(3*ax3,2*bx2,cx)
	eq3 = equation_degrees3(ax3,bx2,cx,d , Derivative.root)
	eq3.roots()
	print("Extermom's: " ,eq3.extermom)
