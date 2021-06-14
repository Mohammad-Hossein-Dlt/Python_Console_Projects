import os
import math
os.system("cls")
# لطفا معادله ها را با فرمت زیر وارد کنید و دقت کنید که بین جمله های معادله فاصله نباشد

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
			# a>0 b,c!=0
			if self.a>0 and self.b>0 and self.c>0:
				# "معادله 2 ریشه (-) دارد . نمودار از ناحیه 4 نمیگذرد"
				return "The equation has 2(-) roots and The function diagram Do Not passes through area 4" 
			elif self.a>0 and self.b>0 and self.c<0:
				# "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
				return "The equation has a (-) root and a (+) root and The function diagram passes through All areas" 
			elif self.a>0 and self.b<0 and self.c>0: 
				# "معادله 2 ریشه (+) دارد و نمودار از ناحیه 3 نمیگذزد"
				return "The equation has 2(+) roots and The function diagram Do Not passes through area 3"
			elif self.a>0 and self.b<0 and self.c<0:
				# "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
				return "The equation has 2(-) roots and The function diagram passes through All areas"
			# a>0 b,c==0
			elif self.a>0 and self.b==0 and self.c==0: 
				# "ریشه معادله 0 است و نمودار از ناحیه 1 و 2 میگذزد"
				return "The equation root is 0 and The function diagram passes through area 1 and 2"
			elif self.a>0 and self.b>0 and self.c==0: 
				# "معادله 1 ریشه (-) و یک ریشه 0 دارد و نمودار از  ناحیه 4 نمیگذزد"
				return "The equation has a (-) and a 0 root and The function diagram Do Not passes through area 4"
			elif self.a>0 and self.b<0 and self.c==0: 
				#"معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از 3 ناحیه نمیگذزد"
				return "The equation has a (+) and a 0 roo and The function diagram Do Not passes through area 3"
			elif self.a>0 and self.b==0 and self.c<0:
				# "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
				return "The equation has a (+) and (-) root and The function diagram passes through All areas"
			#a<0
			elif self.a<0 and self.b>0 and self.c>0:
				# "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
				return "The equation has a (+) and (-) root and The function diagram passes through All areas"
			elif self.a<0 and self.b>0 and self.c<0:
				# "معادله 2 ریشه (+) دارد و نمودار از ناحیه 2 نمیگذزد"
				return "The equation has 2 (+) roots and The function diagram Do Not passes through area 2" 
			elif self.a<0 and self.b<0 and self.c>0:
				# "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
				return "The equation has a (+) and (-) root and The function diagram passes through All areas"
			elif self.a<0 and self.b<0 and self.c<0:
				# "معادله 2 ریشه (-) دارد و نمودار از ناحیه 1 نمیگذزد"
				return "The equation has 2 (-) root and The function diagram ِ Do Not passes through area 1" 
			#a<0 b,c==0
			elif self.a<0 and self.b==0 and self.c==0:
				# "معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از  ناحیه 3 و 4 میگذزد"
				return "The equation has a (+) and 0 root and The function diagram passes through area 3 and 4"
			elif self.a<0 and self.b>0 and self.c==0:
				#"معادله 1 ریشه (+) و یک ریشه 0 دارد و نمودار از  ناحیه 2 نمیگذزد"
				return "The equation has a (+) 0 root and The function diagram passes Do Not through area 2"
			elif self.a<0 and self.b<0 and self.c==0:
				# "معادله 1 ریشه (-) و یک ریشه 0 دارد و نمودار از ناحیه 1 نمیگذزد"
				return "The equation has and (-) and 0 roots and The function diagram Do Not passes through area 1"
			elif self.a<0 and self.b==0 and self.c>0:
				# "معادله 1 ریشه (+) و یک ریشه (-) دارد و نمودار از 4 ناحیه میگذزد"
				return "The equation has a (+) and (-) root and The function diagram passes through All areas"
		if self.delta == 0:
			if self.a>0 and self.b>0 and self.c>0 : 
				# "معادله 1  (-) دارد و نمودار از  ناحیه 1 و 2 میگذزد"
				return "The equation has a (-) root and The function diagram passes through areas 1 and 2"
			elif self.a>0 and self.b<0 and self.c>0 :
				# "معادله 1 ریشه (+) دارد و نمودار از 4 ناحیه میگذزد"
				return "The equation has a (+) root and The function diagram passes through areas 1 and 2"
			elif self.a>0 and self.b==0 and self.c==0 : 
				# "معادله 1 ریشه 0 دارد و نمودار از  ناحیه 1 و 2 میگذزد"
				return "The equation root is 0 and The function diagram passes through areas 1 and 2"
			elif self.a<0 and self.b==0 and self.c==0 :
				# "معادله 1 ریشه 0 دارد و نمودار از ناحیه 3 و 4 میگذزد"
				return "The equation root is 0 and The function diagram passes through areas 3 and 4"
			elif self.a<0 and self.b>0 and self.c<0 : 
				# "معادله 1 ریشه (+) دارد و نمودار از ناحیه 3 و 4 میگذزد"
				return "The equation has a (+) root and The function diagram passes through areas 3 and 4"
			elif self.a<0 and self.b<0 and self.c<0 : 
				# "معادله یک ریشه (-) دارد و نمودار از  ناحیه 3 و 4 میگذزد"
				return "The equation has (-) root and The function diagram passes through areas 3 and 4"
		elif self.delta < 0:
			if self.a>0 and self.b>0 and self.c>0 : 
				# "معادله ریشه ندارد و نمودار از  ناحیه 1 و 2 میگذزد"
				return "The equation has no roots and The function diagram passes through areas 1 and 2"
			elif self.a>0 and self.b<0 and self.c>0 : 
				# "معادله ریشه ندارد و نمودار از  ناحیه 1 و 2 میگذزد"
				return "The equation has no roots and The function diagram passes through areas 1 and 2"
			elif self.a>0 and self.b==0 and self.c>0 : 
				# "معادله ریشه ندارد و نمودار از  ناحیه 1 و 2 میگذزد"
				return "The equation has no roots and The function diagram passes through areas 1 and 2"
			elif self.a<0 and self.b==0 and self.c<0 : 
				# "معادله ریشه ندارد و نمودار از  ناحیه 3 و 4 میگذزد"
				return "The equation has no roots and The function diagram passes through areas 3 and 4"
			elif self.a<0 and self.b>0 and self.c<0 : 
				# "معادله ریشه ندارد و نمودار از  ناحیه 3 و 4 میگذزد"
				return "The equation has no roots and The function diagram passes through areas 3 and 4"
			elif self.a<0 and self.b<0 and self.c<0 : 
				# "معادله ریشه ندارد و نمودار از  ناحیه 3 و 4 میگذزد"
				return "The equation has no roots and The function diagram passes through areas 3 and 4"

class equation_degrees3:
	def __init__(self , ax3 , bx2 , cx , d , ex):
		self.ax3 = ax3/ax3
		self.bx2 = bx2/ax3
		self.cx = cx/ax3
		self.d = d/ax3
		self.p = self.cx - ((self.bx2**2)/3)
		self.q = (( 2 * ( self.bx2 ** 3 ) / 27 ) - (( self.bx2 * self.cx ) / 3)) + self.d
		self.delta = (( self.q**2 ) / 4 ) + (( self.p**3 ) / 27)
		# "اگر  0 > دلتا معادله 3 ریشه دارد "
		# "اگر 0 = دلتا معادله 2 ریشه دارد "
		# "اگر 0 < دلتا معادله 1 ریشه دارد "
		if len(ex) != 0:
			self.ex1 = ax3 * ( ex[0] ** 3 ) + bx2*( ex[0] ** 2 ) + cx * ex[0] + d
			self.ex2 = ax3 * ( ex[1] ** 3 ) + bx2*( ex[1] ** 2 ) + cx * ex[1] + d
			self.extermom = [(ex[0] , round(self.ex1,4)) , (ex[1] , round(self.ex2,4))]
		else:
			self.ex1 = 0
			self.ex2 = 0
			self.extermom = "Extermom Does Not Exist !!!!"
	def roots(self):
		# "برای تعیین تعداد ریشه ها میتوان از دلتا استفاده کرد ولی گاهی بدیل نزدیکی بسیار زیاد دلتا به عدد 0 از طرف منفی و مثبت  سیستم این عدد را گرد میکند"
		#  مثلا ممکن است مقدار واقعی دلتا عددی مثبت یا منفی باشد ولی سیستم آن را 0 در نظر میگیرد
		# " برای کنترول و رفع این مشکل تا حد زیاد ، از اکسترمم های تابع کمک گرفتیم "
		if (( self.ex1 > 0 and self.ex2 > 0 ) or ( self.ex1 < 0 and self.ex2 < 0) ) or (self.ex1 == 0 and self.ex2 == 0) :
			# " بدلیل اینکه بعضی مواقع عدد قرار گرفته در متد "توان" منفی میشود و این متد فقظ اعداد مثبت را میتواند به توان برساند  با تعریف دو متغییر و دو شرط زیر این مشکل را کنترول کردیم  "
			# استفاده از متد توان در این بلاک شرط و بلاک شرط پایینی بدلیل جذر گربفتن با فرجه 3 است چون متد جذر در کتابخانه ریاضی فقط ریشه دوم عدد را برمیگرداند
			n = 1
			m = 1
			if (-self.q/2 ) + math.sqrt(self.delta) < 0 : n = -n
			if (-self.q/2 ) - math.sqrt(self.delta) < 0 : m = -m
			x = ( n * math.pow(  n*( (-self.q/2 ) + math.sqrt(self.delta)) , 1/3 ) ) +  (  m * math.pow( m * (( -self.q/2 ) - math.sqrt(self.delta)) , 1/3 ) ) - (self.bx2/3)
			print("Root: " , round(x,4))
		if ( ( self.ex1 == 0 ) and ( self.ex2 < 0 or self.ex2 > 0)) or (( self.ex2 == 0 ) and ( self.ex1 < 0 or self.ex1 > 0)) :
			# "در این قسمت هم مشکل قسمت قبل وجود دارد و به همان روش کنترول کردیم  "
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

equation = str(input("Enter Equation:\n"))
# برای ساخت لیست از جمله های معادله زمانی که بین جمله ها فاصله نیست ، از حلقه زیر استفاده کردیم تا بر اساس مثبت یا منفی بودن هر جمله ، قبل از علامت آن جمله فاصله بیوفتد
for i in ["+","-"] : equation = equation.replace(i,f" {i}")
equation = equation.split(" ")
if '' in equation : equation.remove('')
#  برای تشخیض 1 و -1 در
# x.. , -x..
# از حلقه و شرط های زیر استفاده کردیم
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

