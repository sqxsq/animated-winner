import pygame

class Ship:
	"""定义Ship类"""
	def __init__(self,ai_game):
		"""初始化飞船及其位置"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#获取飞船图像
		self.image = pygame.image.load('image/ship.bmp')
		#获取飞船外接矩形
		self.rect = self.image.get_rect()
		#设置飞船位置
		self.rect.midbottom = self.screen_rect.midbottom

	def blitmyship(self):
		"""在指定位置绘制船"""
		self.screen.blit(self.image,self.rect)

