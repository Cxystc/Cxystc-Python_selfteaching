class Instrument():
	"""docstring for Instrument"""
	def __init__(self, price,weight,age):
		self.price = price
		self.weight = weight
		self.age = age
	def buy_it(self):
		print ('The price of the instrument is ' + self.price +'.')
	def seld_it(self):
		print ('The instrument has been used for ' + self.age + 'year.')
	def move_it(self):
		print ('The instrument weight ' + self.weight + ' kilograms.')
violin = Instrument("16000","4","5")
violin.buy_it()
violin.seld_it()
violin.move_it()

# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg


class Piano (Instrument):
	def __init__(self, price,weight,age):
		self.price = price
		self.weight = weight
		self.age = age
		super(Instrument, self).__init__()
	def seld_it (self):
		print("You cannot seld your piano ,no one would buy it,it is yours partern！")
		# 关于引号字符串出现问题

pianos = Piano("300000","200","10")	
pianos.seld_it()
