import unittest
from class_myCar import Car

class CarTestCase(unittest.TestCase):
	"""Car类的单元测试"""

	def setUp(self):
		"""创建一个类，在后面的测试方法中可以直接使用，就不需要每次都创建了"""
		self.my_car=Car('A4','奥迪','2021')
		self.information='2021 奥迪 A4'
		self.mile0=100
		self.mile1=50

	def test_descriptive_name(self):
		"""测试get_descriptive_name方法是否能正确得到车辆信息"""
		self.assertEqual(self.my_car.get_descriptive_name(),self.information)

	def test_update_odometer(self):
		"""测试update_odometer方法是否能得到正确结果"""
		self.my_car.update_odometer(100)
		self.assertEqual(self.my_car.odometer_reading,self.mile0)
		self.my_car.update_odometer(10)
		self.assertEqual(self.my_car.odometer_reading,self.mile0)

	def test_increment_odometer(self):
		"""测试increment_odometer方法是否能得到正确结果"""
		self.my_car.increment_odometer(50)
		self.assertEqual(self.my_car.odometer_reading,self.mile1)

if __name__=='__main__':
	unittest.main()



