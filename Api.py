import math
class reverse:
	string=''
	def __init__(self,string):
		self.string=string
	def get_text(self):
		textlist=self.string.split()
		textlist.reverse()
		return ' '.join(textlist)

class upper:
	string=''
	def __init__(self,string):
		self.string=string
	def get_text(self):
		return self.string.upper()

class rec:
	l=''
	w=''
	def __init__(self,l,w):
		self.l=l
		self.w=w
	def get_answer(self):
		return self.l*self.w
 
class circle:
	r=''
	def __init__(self,r):
		self.r=r
	def get_area(self):
		return math.pi*self.r**2 
	def get_per(self):
		return 2*self.r*math.pi
        	    