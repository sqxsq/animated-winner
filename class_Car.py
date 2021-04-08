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

my_car = Car('A4','奥迪',2021)
print(my_car.get_descriptive_name())
my_car.read_odometer()
#使用方法修改属性的值
my_car.update_odometer(100)
my_car.read_odometer()

my_car.update_odometer(10)

#直接修改属性的值
my_car.odometer_reading=10
my_car.read_odometer()

my_car.increment_odometer(10)
my_car.read_odometer()

class Battary:
	"""docstring for Battary"""
	def __init__(self, battary_size=75):
		self.battary_size=battary_size

	def describe_battary(self):
		"""打印电动汽车的电瓶信息"""
		print(f'This car has a {self.battary_size}-kwh battary.')

#创建Car的子类ElectricCar（继承父类Car）
#父类（超类superclass）必须在子类前面定义，且必须在同一个文件中存在
#子类的方法与父类重复时，会忽略父类的方法，而是调用子类的方法
class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self,model,make,year):
		"""先初始化父类的属性，再初始化电动汽车的独有属性。"""
		#调用父类的方法__init__()
		super(ElectricCar, self).__init__(model,make,year)
		#定义自己的属性,将Battary类创建的实例当作属性
		self.battary = Battary()
	#定义自己的方法
	def get_range(self):
		"""打印续航里程"""
		if self.battary.battary_size==75:
			range=160
		if self.battary.battary_size==100:
			range=350
		print(f'还能续航{range}miles')
	
my_electriccar = ElectricCar('A5','奥迪',2021)
print(my_electriccar.get_descriptive_name())

my_electriccar.battary.describe_battary()
my_electriccar.get_range()

		
