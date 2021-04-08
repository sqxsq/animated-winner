class Car:
	"""练习类的使用"""
	#self是必须有的参数，且自动传递
	#类中的函数成为方法
	#方法__init__()是python的默认方法，当使用类创建实例时会自动运行此方法，方法名称不可修改
	def __init__(self,model,make,year):
		self.model=model
		self.make=make
		self.year=year
		self.odometer_reading=0
		#odometer_reading:已行驶里程数

	def get_descriptive_name(self):
		"""返回车的信息"""
		long_information=f"{self.year} {self.make} {self.model}"
		return long_information
	
	def read_odometer(self):
		"""打印里程数"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self,mileage):
		"""更新里程数"""
		if mileage>self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("里程数不能调小")

	def increment_odometer(self,miles):
		"""上调里程数"""
		self.odometer_reading += miles