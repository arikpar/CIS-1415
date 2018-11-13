class CellPhone:
	def __init__(self,manufact = '',model='' ,retail_price = 0):
		self.manufact = manufact
		self.model = model
		self.retail_price = retail_price
		
	def set_manufact(self,manufact):
		self.manufact = manufact
		
	def set_model(self,model):
		self.model = model
	
	def set_retail_price(self,retail_price):
		self.retail_price = retail_price
		
	def get_manufact(self):
		return self.manufact
		
	def get_model(self):
		return self.model
		
	def get_retail_price(self):
		return self.retail_price
		
		
phone = CellPhone()
phone.set_manufact(input('Enter the Manufacturer: '))
phone.set_model(input('Enter the model number: '))
phone.set_retail_price(input('Enter the retail price: '))
print('Here is the data that you entered:')
print('Manufacturer:', phone.get_manufact())
print('Model Number:', phone.get_model())
print('Retail Price: $%s' % phone.get_retail_price())
